<template>
    <div class="main-content">
		<div class="main-content-inner">
			<!-- 面包屑 -->
			<div class="breadcrumbs" id="breadcrumbs">
				<ul class="breadcrumb">
					<li>
						<i class="ace-icon fa fa-home home-icon"></i>
						<a href="/">首页</a>
					</li>
					<li>
						<a href="/" class="active">{{title}}</a>
					</li>
				</ul>
			</div>
			<!-- 右侧主要内容 -->
			<div class="page-content">
				<div class="page-header">
					<h1>
						{{title}}
					</h1>
				</div>
                <p class="tip clearfix" v-if="limits_list.length>0">
                    根据教务处预选数据，你能选
                    <span v-for="limits in limits_list" :key="'limits'+limits.id">
                        <span v-for="week in weekArray" :key="'week'+week.week" v-if="week.week == limits.week">{{week.name}}</span>
                        <span v-for="item in courseItem" :key="'item'+item.id" v-if="item.id == limits.csItemId">{{item.csItemName}}</span>
                    </span>
                    的课程，您还可以选择{{parseInt(this.sysSetting.maxCourseCount)-this.selectCoutseList.length}}节课。
                    <button class="pull-right btn btn-primary btn-xs" @click="resetSelectCourse">刷新选课情况</button>
                </p>
                <div class="table-responsive">
                    <table class="table table-bordered">
                        <thead>
                            <tr>
                                <th class="little">课程名称</th>
                                <th v-for="limits in limits_list" :key="'limits'+limits.id">
                                    <span v-for="week in weekArray" :key="'week'+week.week" v-if="week.week == limits.week">{{week.name}}</span>
                                    <span v-for="item in courseItem" :key="'item'+item.id" v-if="item.id == limits.csItemId">{{item.csItemName}}</span>
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="course in course_list" :key="'course'+course.id" v-if="limits_list.length>0 && hasClass(course)">
                                <td>{{course.courseName}}</td>
                                <td v-for="limits in limits_list" :key="'limits'+limits.id">
                                    <div v-for="courseClass in courseClassList"
										 :key="'courseClass'+courseClass.id"
										 :class="['courseClassCell',{'bg-info':isSelect(courseClass)=='no'}]"
										 v-if="course.id == courseClass.courseId
                                            && limits.csItemId == courseClass.csItemId
                                            && limits.week == courseClass.week
                                            && courseClass.courseUnitId == limits.courseUnitId"
									>
                                        <div class="cell" v-for="teacher in teacher_list" style="padding:5px;min-width:86px;"
											 :key="'teacher'+teacher.id" v-if="courseClass.teacherUid == teacher.teacherId">
                                            <img :src="serverUrl+'/'+teacher.pic" :alt="teacher.name"
												 @click="setTeacher(teacher,courseClass)"
												 width="30px" height="30px" class="pointer" v-if="teacher.pic">
                                            <a href="#" @click.prevent="setTeacher(teacher,courseClass)">{{teacher.name}}</a>
                                        </div>
                                        <div class="cell" style="padding:5px;">
                                            <p>
                                                <span v-for="school in school_list" :key="'school'+school.id" v-if="school.id == courseClass.campus">{{school.codename}}</span>
                                                {{courseClass.areaName}}
                                            </p>
                                            <p>{{courseClass.startWeek}}~{{courseClass.endWeek}} 周</p>
                                            <p>
                                                <span v-html="computedSelectCount(courseClass)"></span>
                                                / 可选<b>{{courseClass.count}}</b> 人，其中男：<b>{{courseClass.countMale?courseClass.countMale:0}}</b> 人，
                                                女：<b>{{courseClass.countFemale?courseClass.countFemale:0}}</b> 人
                                            </p>
                                            
                                            <div v-if="openStatus(courseClass).status ==='noStart'" class="red">
                                                {{openStatus(courseClass).timeRange}}
                                            </div>
                                            <div v-else-if="openStatus(courseClass).status ==='end'" class="red">
                                                {{openStatus(courseClass).timeRange}}
                                            </div>
                                        </div>
                                        <div class="cell">
                                            <span v-if="isSelect(courseClass)=='yes'">
                                                <button
														v-for="(open,index) in courseOpen" :key="'courseOpen'+index"
														class="btn btn-purple btn-sm selectCourseBtn" @click="selectCourseClass(courseClass)"
														v-if="open.week == courseClass.week
                                                        && open.csItemId == courseClass.csItemId
                                                        && today>=open.startDate
                                                        && today<=open.endDate
                                                        && currentTerm.id == open.termId
                                                        && open.courseUnitId == courseClass.courseUnitId"
												>选课</button>
                                            </span>
                                            <button class="btn btn-xs selectCourseBtn" v-else-if="isSelect(courseClass)=='no'">已选择</button>
                                            <span v-else-if="isSelect(courseClass)=='other'" class="selectCourseBtn green">已选择其他课程</span>
                                            <button class="btn btn-sm selectCourseBtn" v-else-if="isSelect(courseClass)=='exceed'">已达到人数上限</button>
                                        </div>
                                    </div>
                                </td>
                            </tr>
                            <tr v-if="limits_list.length==0 || course_list.length==0 ||courseClassList.length==0" class="center">
                                <td :colspan="1+limits_list.length">根据教务处选课预排设置，您没有可选的课程！</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="tipBox" v-if="showTip">
                    <div class="gritter-item-wrapper gritter-info widget-main">
                        <div class="gritter-top"></div>
                        <div class="gritter-item clearfix">
                            <div class="gritter-close pull-right" @click="showTip=false"></div>
                            <div class="gritter-with-image">
                                <img :src="serverUrl+ '/' +currentTeacher.pic" alt="" class="gritter-image">
                                <div class="h4">{{currentTeacher.name}}</div>
                                <p style="min-height:100px">
                                    {{currentTeacher.summary}}
                                </p>
                                <div class="space-6 bg-info"></div>
                                <p>
                                    您查看的是：{{currentTeacher.name}}老师
                                    <span v-for="week in weekArray" :key="'week'+week.week" v-if="week.week == currentCourseClass.week">{{week.name}}</span>
                                    {{currentCourseClass.csItemName}} {{currentCourseClass.courseName}}课，上课地点为：
                                    <span v-for="school in school_list" :key="'school'+school.id" v-if="school.id == currentCourseClass.campus">{{school.codename}}</span>校区{{currentCourseClass.areaName}}
                                    上课时间为：{{currentCourseClass.startWeek}}~{{currentCourseClass.endWeek}}周
                                </p>
                                <div class="col-xs-offset-1 col-xs-10 h5">
                                    <span v-if="isSelect(currentCourseClass)=='yes'">
                                        <button
												v-for="(open,index) in courseOpen" :key="'courseOpen'+index"
												class="btn btn-purple btn-sm btn-block selectCourseBtn"
												@click="selectCourseClass(null)"
												v-if="open.week == currentCourseClass.week
                                                && open.csItemId == currentCourseClass.csItemId
                                                && today>=open.startDate
                                                && today<=open.endDate
                                                && currentTerm.id == open.termId
                                                && open.courseUnitId == currentCourseClass.courseUnitId"
										>确认选择该课程</button>
                                    </span>
                                    <button class="btn btn-sm btn-block selectCourseBtn" v-else-if="isSelect(currentCourseClass)=='no'">已选择</button>
                                    <button class="btn btn-sm btn-block selectCourseBtn" v-else-if="isSelect(currentCourseClass)=='other'">此时间段已选择其他课程</button>
                                    <button class="btn btn-sm btn-block selectCourseBtn" v-else-if="isSelect(currentCourseClass)=='exceed'">已达到人数上限</button>
                                    <span class="btn btn-sm btn-block red">暂未开放</span>
                                    <div v-if="openStatus(currentCourseClass).status ==='noStart'" class="red">
                                        {{openStatus(currentCourseClass).timeRange}}
                                    </div>
                                    <div v-else-if="openStatus(currentCourseClass).status ==='end'" class="red">
                                        {{openStatus(currentCourseClass).timeRange}}
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
			</div>
		</div>
    </div>
</template>
<script>
    export default {
        name:"term",
        data(){
            return {
                title:"选课管理",
                showTip:false,
                courseClassList:[], //能选择的课程安排
                currentTeacher:{}, //当前教师
                currentCourseClass:{},
                currentTerm:{}, //当前期次
                limits_list:[],
                selectCourseCount:{},
                selectCoutseList:[],
                courseOpen:[], //选课是否开放
                today:Date.parse(new Date()),
            }
        },
        computed:{
            course_list(){
                return this.$store.state.course_list;
            },
            courseItem(){
                return this.$store.state.courseItem;
            },
            term_list(){
                return this.$store.state.term_list;
            },
            teacher_list(){
                return this.$store.state.teacher_list;
            },
            school_list(){
                return this.$store.state.school_list;
            },
            sysSetting(){
                return this.$store.state.sysSetting;
            }
        },
        watch:{
            term_list(){
                this.termInfo();
            },
            currentTerm(){
                this.getCourseClass();
                this.getLimitsList();
                this.getSelectCourseCount();
                this.getSelectCourseList();
            }
        },
        methods:{
            init(){
                if(this.$store.state.teacher_list.length==0){
                    this.$store.dispatch("getTeacherList");
                }
                if(this.$store.state.term_list.length==0){
                    this.$store.dispatch("getTermList");
                }else{
                    this.termInfo();
                }
                if(this.$store.state.courseItem.length==0){
                    this.$store.dispatch("getCourseItem");
                }
                if(this.$store.state.course_list.length==0){
                    this.$store.dispatch("getCourseList");
                }
                if(this.$store.state.school_list.length==0){
                    this.$store.dispatch("getCodeTypeList",{parentKey:'school'});
                }
                this.getCourseOpens();
            },
            getCourseClass(){
                //学生可选课程列表
                const _this =this;
                const path = "/api/term/"+this.currentTerm.id+"/student/"+this.user.username+"/course/classes";
                this.emitAjax({
                    path,
                    success:function(result){
                        _this.courseClassList = result;
                    }
                });
            },
            getLimitsList(){
                //选课限制
                const _this = this;
                this.emitAjax({
                    path:"/api/courses/limits",
                    data:{termId:this.currentTerm.id,uid:this.user.username},
                    success:function(result){
                        _this.limits_list = result;
                    }
                });
            },
            getCourseOpens(){
                //获取选课开放列表
                const _this = this;
                this.emitAjax({
                    path:"/api/course/classes/open_status",
                    success:function(result){
                        _this.courseOpen = result.openstatus;
                        _this.today = result.timestamp;
                    }
                })
            },
            getSelectCourseCount(){
                //获取课程已选的数量
                const _this = this;
                this.emitAjax({
                    path:"/api/course/status",
                    data:{term:this.currentTerm.id,studentUid:this.user.username},
                    success:function(result){
                        _this.selectCourseCount = result;
                        _this.$store.commit("setLoading",false);
                    },
                    error:function(){
                        _this.$store.commit("setLoading",false);
                    }
                });
            },
            getSelectCourseList(){
                //当前学生的已选课列表
                const _this = this;
                this.emitAjax({
                    path:"/api/term/"+this.currentTerm.id+"/student/"+this.user.username+"/course/classes/choosed",
                    success:function(result){
                        _this.selectCoutseList = result;
                    }
                });
            },
            setTeacher(teacher,course){
                this.showTip = true;
                this.currentTeacher = Object.assign({},teacher);
                this.currentCourseClass = Object.assign({},course);
            },
            termInfo(){
                //获取当前期次
                let flag = false;
                for (let index = 0; index < this.term_list.length; index++) {
                    const term = this.term_list[index];
                    if(term.currentTerm==1){
                        this.currentTerm = term;
                        flag = true;
                        break;
                    }
                }
                if(!flag){
                    this.currentTerm = this.term_list[0];
                }
            },
            selectCourseClass(courseClass){
                //选择课程
                if(courseClass){
                    this.currentCourseClass = Object.assign({},courseClass);
                }
                if(this.selectCoutseList.length >=this.sysSetting.maxCourseCount){
                    alert("您的选课数量已达上线！");
                    return false;
                }
                if(confirm("是否选择"+this.currentCourseClass.teacherName+"老师的"+this.currentCourseClass.courseName+"课程")){
                    const _this = this;
                    this.$store.commit("setLoading",true);
                    const option = {
                        path:"/api/courses/students",
                        data:{
                            courseClassId:this.currentCourseClass.id,
                            studentUid:this.user.username,
                            teacherUid:this.currentCourseClass.teacherUid,
                            teacherName:this.currentCourseClass.teacherName,
                        },
                        type:"POST",
                        success:function(result){
                            _this.$store.commit("setLoading",false);
                            alert("选课完成");
                            _this.getSelectCourseList();
                            _this.getSelectCourseCount();
                        },
                        error:function(){
                            _this.$store.commit("setLoading",false);
                        }
                    }
                    this.emitAjax(option);
                }
            },
            resetSelectCourse(){
                //刷新选课情况
                this.$store.commit("setLoading",true);
                this.getSelectCourseList();
                this.getSelectCourseCount();
            },
            hasClass(course){
                //判断这个课程有没有排课
                let isTrue = false;
                for (let index = 0; index < this.courseClassList.length; index++) {
                    const courseClass = this.courseClassList[index];
                    if(courseClass.courseId == course.id){
                        isTrue = true;
                        break;
                    }
                }
                return isTrue;
            },
            computedSelectCount(courseClass){
                //计算已选人数
                let count = 0 ;
                let string = "";
                const selectCourse = this.selectCourseCount[""+courseClass.id];
                let male = 0;
                let female = 0;
                if(selectCourse){
                    female = selectCourse["2"]?selectCourse["2"]:0;
                    male = selectCourse["1"]?selectCourse["1"]:0;
                    count = female + male;
                }
                if(count>0){
                    string = "已选 <b>"+count+"</b> 人，其中男 <b>"+male+"</b> 人，女 <b>"+female+"</b> 人";
                }else{
                    string = "已选 <b>"+count+"</b> 人";
                }
                return string;
            },
            isSelect(currentClass){
                //判断是否已经选择了
                let bool = 'yes';
                //循环学生所有的课程
                for (let index = 0; index < this.courseClassList.length; index++) {
                    const courseClass = this.courseClassList[index];
                    if(bool == 'no'){break}
                    //循环学生选择了的课程
                    for (let index = 0; index < this.selectCoutseList.length; index++) {
                        const selectCourse = this.selectCoutseList[index];
                        if(selectCourse.courseClassId == courseClass.id){
                            //锁定已选课程信息
                            if(currentClass.id == courseClass.id){
                                //学生选择了这门课
                                bool = "no";
                                break;
                            }else if(courseClass.week == currentClass.week && courseClass.csItemId == currentClass.csItemId){
                                //这节课没有选择但是 这个节点已经选择了其他的课程
                                bool = "other";
                                break;
                            }
                        }
                    }
                }
                //课程的剩余情况
                if( bool == 'yes'){
                    const countMale = currentClass.countMale?parseInt(currentClass.countMale):0;
                    const countFemale = currentClass.countFemale?parseInt(currentClass.countFemale):0;
                    const selectCount = this.selectCourseCount[currentClass.id]?this.selectCourseCount[currentClass.id]:{};
                    const _countMale = selectCount[1]?parseInt(selectCount[1]):0;
                    const _countFemale = selectCount[2]?parseInt(selectCount[2]):0;
                    if(this.user.gender==1 && _countMale>=countMale || this.user.gender==2 && _countFemale>=countFemale){
                        bool='exceed';
                    }
                }
                return bool;
            },
            openStatus(courseClass){
                //判断课程有没有在开放期间内
                for (let index = 0; index < this.courseOpen.length; index++) {
                    const open =  this.courseOpen[index];
                    if(open.week == courseClass.week&&
                        open.csItemId == courseClass.csItemId&&
                        this.currentTerm.id == open.termId &&
                        courseClass.courseUnitId == open.courseUnitId
                    ){
                        const timeRange = this.moment(open.startDate).format("YYYY/MM/DD HH:mm:ss") +" -- "+ this.moment(open.endDate).format("YYYY/MM/DD HH:mm:ss");
                        if(this.today<open.startDate){
                            return {
                                status:"noStart",
                                timeRange:"暂未开放，开放时间："+timeRange,
                            }
                        }else if(this.today>open.endDate){
                            return {
                                status:"end",
                                timeRange:"选课结束，开放时间："+timeRange,
                            }
                        }
                    }
                }
                return {
                    status:"yes",
                    timeRange:"",
                }
            }
        },
        mounted(){
            this.init();
        }
    };
</script>




// WEBPACK FOOTER //
// src/components/selectCourse/selectCourse.vue