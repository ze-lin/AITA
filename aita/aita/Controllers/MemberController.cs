using aita.Models;
using aita.Services;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.IO;

namespace aita.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class MemberController : ControllerBase
    {
        private readonly MemberService _memberService;

        public MemberController(MemberService memberService)
        {
            _memberService = memberService;
        }


        [Route("signup")]
        [HttpPost]
        [HttpOptions]
        public ActionResult<string> SignUp([FromForm] string usr, [FromForm] string pwd, [FromForm] string role)
        {
            Member tmpMember = _memberService.Get(usr);

            if(tmpMember == null)
            {
                Member newUsr = new Member();
                newUsr.usr = usr;
                newUsr.pwd = pwd;
                newUsr.role = role;
                var tmpStream = new MemoryStream();
                var files = Request.Form.Files;
                var image = files.GetFile("image");
                image.CopyTo(tmpStream);
                newUsr.pic = Convert.ToBase64String(tmpStream.ToArray());
                newUsr.date = DateTime.Now.ToShortDateString().ToString();
                _memberService.Create(newUsr);

                return "Success!";
            }
            else
            {
                return "Taken";
            }
        }

        [Route("signin")]
        [HttpPost]
        public JsonResult SignIn([FromForm] string usr, [FromForm] string pwd)
        {
            Member tmpMember =_memberService.Get(usr);
            if(tmpMember != null && tmpMember.pwd == pwd)
            {
                return new JsonResult(new { status=true, role= tmpMember.role});
            }
            return new JsonResult(new { status=false });

        }

        [Route("logout")]
        [HttpGet]
        public ActionResult<string> Logout()
        {
            return "Success!";
        }


        [Route("getinfo")]
        [HttpGet]
        public JsonResult GetUsrInfo([FromQuery] string usr)
        {
            Member tmpMember = _memberService.Get(usr);
            return new JsonResult(new { usr=usr, pwd= tmpMember.pwd, role= tmpMember.role, date=tmpMember.date });
        }

        [Route("updateinfo")]
        [HttpPost]
        public ActionResult<string> UpdateUsrInfo([FromForm] string usr, [FromForm] string pwd)
        {
            Member tmpMember = _memberService.Get(usr);
            if(pwd != "")
            {
                tmpMember.pwd = pwd;
            }
            var files = Request.Form.Files;
            var tmpStream = new MemoryStream();
            var image = files.GetFile("file");
            image.CopyTo(tmpStream);
            tmpMember.pic = Convert.ToBase64String(tmpStream.ToArray());
            _memberService.Update(usr, tmpMember);
            return "Success!";
        }

        [Route("updatepwd")]
        [HttpGet]
        public ActionResult<string> UpdateUsrPwd([FromQuery] string usr, [FromQuery] string pwd)
        {
            Member tmpMember = _memberService.Get(usr);
            if(pwd != "")
            {
                tmpMember.pwd = pwd;
            }
            _memberService.Update(usr, tmpMember);
            return "Success!";
        }

        [Route("getpic")]
        [HttpGet]
        public ActionResult<string> GetUsrPic([FromQuery] string usr)
        {
            Member tmpMember = _memberService.Get(usr);
            return tmpMember.pic;
        }
    }
}
