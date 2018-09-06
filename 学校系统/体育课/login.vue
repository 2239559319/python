<template>
    <div class="login">
        <div class="login-container">
            <div class="center">
                <h1>
                    <i class="ace-icon fa fa-flask green"></i>
                    <span class="red">体育选课系统</span>
                    <span class="white" id="id-text2"></span>
                </h1>
            </div>
            <div class="space-6"></div>
            <div class="position-relative">
                <div id="login-box" class="login-box visible widget-box no-border">
                    <div class="widget-body" v-if="isSingle">
                        <div class="widget-main">
                            <h4 class="header blue lighter bigger">
                                <i class="ace-icon fa fa-coffee green"></i>
                                请输入您的帐号密码
                            </h4>
                            <div class="space-6"></div>
                            <form @keyup="enterLogin($event)">
                                <fieldset>
                                    <label class="block clearfix">
                                        <span class="block input-icon input-icon-right">
                                            <input type="text" class="form-control" v-model="username" placeholder="用户名" />
                                            <i class="ace-icon fa fa-user"></i>
                                        </span>
                                    </label>
                                    <label class="block clearfix">
                                        <span class="block input-icon input-icon-right">
                                            <input type="password" class="form-control" v-model="password" placeholder="密码" />
                                            <i class="ace-icon fa fa-lock"></i>
                                        </span>
                                    </label>
									<!-- <label class="block clearfix row">
										<span class="block input-icon input-icon-right col-xs-6">
											<input type="text" class="form-control" v-model="verifyCode" placeholder="验证码" />
										</span>
										<span class="block input-icon input-icon-right col-xs-6">
											<img :src="serverUrl+'/admin/login/getVerify'" class="verifyCode" alt="验证码" @click="refreshVerifyCode">
										</span>
									</label> -->
                                    <div class="space"></div>
                                    <div class="clearfix">
                                        <label class="inline">
                                            <input type="checkbox" class="ace" v-model="remeberme" />
                                            <span class="lbl"> 记住帐号？</span>
                                        </label>
                                        <button type="button" class="width-35 pull-right btn btn-sm btn-primary" @click="login">
                                            <i class="ace-icon fa fa-key"></i>
                                            <span class="bigger-110">登录</span>
                                        </button>
                                    </div>
                                    <div class="space-4"></div>
                                </fieldset>
                            </form>
                        </div>
                        <div class="toolbar clearfix white">
                            <span class="col-xs-12">
                                <h5>如果没有帐号，请联系相关管理人员添加帐号。</h5>
                            </span>
                        </div>
                    </div>
                    <div class="widget-body" v-if="!isSingle">
                        <div class="widget-main">
                            <h4 class="header blue lighter bigger">
                                <i class="ace-icon fa fa-coffee green"></i>
                                请选择一个身份登录
                            </h4>
                            <div class="space-6"></div>
                            <fieldset>
                                <label v-if="role_list" v-for="role in role_list" :key="'role'+role.org_id" class="block">
                                    <input type="radio" class="ace" @click="selectRoleLogin(role)" name="role">
                                    <span class="lbl"> {{role.o_name}}-{{role.g_name}}</span>
                                </label>
                                <div class="space"></div>
                                <div class="clearfix">
                                    <button type="button" class="width-35 btn btn-sm btn-primary" @click="submitRoleLogin">
                                        <span class="bigger-110">确定</span>
                                    </button>
                                </div>
                                <div class="space-4"></div>
                            </fieldset>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
	</div>
</template>
<script>
import { setLocalData, delLocalData } from "../assets/common.js";
import { weakPassword } from '../config/config';
export default {
    name: "login",
    data() {
        return {
            username: "",
            password: "",
            verifyCode: "",
            remeberme: false,
            role_list: [
                {
                    org_id: 19,
                    org_name: "研究生院"
                }
            ],
            isSingle: true,
            selectRole: {},
        }
    },
    methods: {
        login() {
            //登录
            if (!this.isNotEmpty()) { return false };
            const _this = this;
            let data = {
                username: this.username.replace(/\s+/g, ""),
                password: this.password.replace(/\s+/g, ""),
            }
            this.remeberMe();
            const path = "/api/login";
            const option = {
                path,
                data,
                type: "POST",
                success: function (result) {
                    _this.loginSuccess(result);
                },
                error: function () {
                    delLocalData();
                    _this.refreshVerifyCode();
                }
            }
            this.emitAjax(option);
        },
        loginSuccess(result) {
            //登录成功做处理
            if (typeof result == "object") {
                //判断是否为弱密码
                if (weakPassword.indexOf(this.password) >= 0) {
                    localStorage.setItem("weak", "role" + result.role);
                }
                setLocalData(result);
                window.location.href = this.pathName + '/';
            } else {
                alert(result);
            }
        },
        selectRoleLogin(role) {
            this.selectRole = role;
        },
        submitRoleLogin() {
            const _this = this;
            let data = Object.assign({}, this.selectRole, {
                flag: true,
            })
            const url = this.serverUrl + "/admin/login/login";
            this.emitAjax(url, data, function (result) {
                _this.loginSuccess(result);
            }, function () {
                delLocalData();
                // _this.refreshVerifyCode();
            })
        },
        refreshVerifyCode() {
            //刷新验证码
            this.verifyCode = "";
            $(".verifyCode").attr("src", this.serverUrl + '/admin/login/getVerify?code=' + Math.random());
        },
        remeberMe() {
            //记住帐号
            if (this.remeberme) {
                localStorage.setItem("remeberMe", this.username);
            } else {
                localStorage.removeItem("remeberMe");
            }
        },
        info() {
            //页面初始化
            //this.refreshVerifyCode();
            const remeberMe = localStorage.getItem("remeberMe");
            const leftMenu = localStorage.getItem("leftMenu");
            const Authorization = localStorage.getItem("Authorization");
            if (remeberMe) {
                this.username = remeberMe;
                this.remeberme = true;
            }
            if (leftMenu && Authorization && this.user.username) {
                this.$router.push(this.pathName + "/");
            }
        },
        enterLogin(event) {
            if (event.type == "keyup" && event.key == "Enter") {
                this.login();
            }
        },
        isNotEmpty() {
            if (this.username == "") {
                alert("请填写用户名！");
                return false;
            }
            if (this.password == "") {
                alert("请填写密码！");
                return false;
            }
            return true;
        },
    },
    mounted() {
        this.info();
    }
};
</script>
<style>
.verifyCode {
	max-width: 100%;
	height: auto;
}
</style>



// WEBPACK FOOTER //
// src/components/login.vue