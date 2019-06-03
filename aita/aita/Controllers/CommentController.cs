using aita.Models;
using aita.Services;
using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.IO;

namespace aita.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class CommentController
    {
        private readonly CommentService _commentService;

        public CommentController(CommentService commentService)
        {
            _commentService = commentService;
        }

        [Route("add")]
        [HttpGet]
        public ActionResult<string> AddComment([FromQuery] string startTime, [FromQuery] string endTime, [FromQuery] string content, [FromQuery] string id)
        {
            Comment newComment = new Comment();
            newComment.content = content;
            newComment.endTime = endTime;
            newComment.startTime = startTime;
            newComment.id = id;

            _commentService.Create(newComment);
            return "Success!";
        }

        [Route("get")]
        [HttpGet]
        public JsonResult GetComment([FromQuery] string id)
        {
            var JsonBody = new Dictionary<int, Dictionary<string, string>>();
            var result = _commentService.GetAll(id);
            int i = 0;
            foreach(var commet in result)
            {
                var tmpDic = new Dictionary<string, string>();
                tmpDic.Add("startTime", commet.startTime);
                tmpDic.Add("endTime", commet.endTime);
                tmpDic.Add("content", commet.content);
                JsonBody.Add(i++, tmpDic);

            }
            return new JsonResult(JsonBody);

        }
    }
}
