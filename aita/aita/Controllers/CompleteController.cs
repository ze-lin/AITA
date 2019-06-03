using aita.Models;
using aita.Services;
using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;

namespace aita.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class CompleteController : ControllerBase
    {
        private readonly CompleteService _completeService;

        private int calcuFocus(Dictionary<string, float> focusDic)
        {
            float result = 100 - focusDic["anger"] - focusDic["disgust"] - focusDic["fear"] - focusDic["sadness"] / 2 - focusDic["surprise"] / 2 -
                focusDic["vector_x"] * 30 - focusDic["vector_y"] * 30;
            if (result < 0)
            {
                result = 0;
            }

            return (int)result;
        }

        private int calcuComplete(Focus focusData)
        {
            if(focusData != null)
            {
                int ans = 100;
                var emotionData = focusData.emotion;
                for(int minute = 0; minute < 10; minute++)
                {
                    int score = 0;
                    for(int second = minute * 60; second < (minute + 1) * 60; second++)
                    {
                        if (emotionData.ContainsKey(Convert.ToString(second)))
                        {
                            score += calcuFocus(emotionData[Convert.ToString(second)]);
                        }
                    }
                    if(score < 2000)
                    {
                        ans -= 10;
                    }
                }
                return ans;
            }
            else
            {
                return 0;
            }
        }


        public CompleteController(CompleteService completeService)
        {
            _completeService = completeService;
        }

        [Route("get")]
        [HttpGet]
        public JsonResult GetCompleteness([FromQuery] string usr)
        {
            var JsonBody = new Dictionary<int, Dictionary<string, string>>();
            var result = _completeService.GetAll(usr);
            int i = 0;
            foreach(var complete in result)
            {
                string id = complete.id;
                var focusResult = _completeService.GetFocus(id, usr);
                var courseResult = _completeService.GetCourse(id);
                var document = courseResult.ToDic();
                document.Add("complete", Convert.ToString(calcuComplete(focusResult)));
                JsonBody.Add(i++, document);
            }
            return new JsonResult(JsonBody);
        }
    }
}
