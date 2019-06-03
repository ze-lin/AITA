using aita.Models;
using aita.Services;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Collections;


namespace aita.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class CourseController: ControllerBase
    {
        private readonly CourseService _courseService;

        public CourseController(CourseService courseService)
        {
            _courseService = courseService;
        }

        [Route("getall")]
        [HttpGet]
        public JsonResult GetAllCourse()
        {
            var courseList = _courseService.GetAll();
            
            var resultList = new ArrayList();
            foreach(Course course in courseList)
            {
                var tmpCourse = course.ToDic();
                resultList.Add(tmpCourse);
            }

            return new JsonResult(resultList);
        }

        [Route("create")]
        [HttpGet]
        public ActionResult<string> CreateCourse([FromQuery] string genre, [FromQuery] string title, [FromQuery] string exam, [FromQuery] string time, [FromQuery] string teacher, [FromQuery] string video, [FromQuery] string article)
        {
            Course newCourse = new Course();
            newCourse.article = article;
            newCourse.view = "0";
            newCourse.title = title;
            newCourse.teacher = teacher;
            newCourse.date = DateTime.Now.ToShortDateString().ToString();
            newCourse.id = DateTime.Now.ToUniversalTime().ToString();
            newCourse.video = video;
            newCourse.genre = genre;
            newCourse.exam = exam;
            newCourse.time = time;

            _courseService.Create(newCourse);

            return "Success!";
        }

        [Route("getallteacher")]
        [HttpGet]
        public JsonResult GetAllTeacher([FromQuery] string teacher)
        {
            var courseList = _courseService.GetAll(teacher);

            var resultList = new ArrayList();
            foreach (Course course in courseList)
            {
                var tmpCourse = course.ToDic();
                resultList.Add(tmpCourse);
            }

            return new JsonResult(resultList);
        }

        [Route("uploadfile")]
        [HttpPost]
        [RequestSizeLimit(500_000_000)]
        public ActionResult<string> UploadFile()
        {
            var files = Request.Form.Files;
            var result = "";
            foreach(var file in files)
            {
                result += file.FileName;
            }
            return result;
        }
    }
}
