using aita.Models;
using aita.Services;
using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;

namespace aita.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class FocusController : ControllerBase
    {
        private readonly FocusService _focusService;

        public FocusController(FocusService focusService)
        {
            _focusService = focusService;
        }

        private float calcuFocus(Dictionary<string, float> focusDic)
        {
            float result = 100 - focusDic["anger"] - focusDic["disgust"] - focusDic["fear"] - focusDic["sadness"]/2 - focusDic["surprise"]/2 -
                focusDic["vector_x"]*30 - focusDic["vector_y"]*30;
            if(result < 0)
            {
                result = 0;
            }

            return result;
        }

        [Route("add")]
        [HttpGet]
        public ActionResult<string> AddFocus([FromQuery] string anger, [FromQuery] string disgust, [FromQuery] string fear, [FromQuery] string vector_z, [FromQuery] string time,
            [FromQuery] string happiness, [FromQuery] string neutral, [FromQuery] string sadness, [FromQuery] string surprise, [FromQuery] string vector_x,
            [FromQuery] string vector_y, [FromQuery] string position_x, [FromQuery] string position_y, [FromQuery] string usr, [FromQuery] string id)
        {
            string cTime = Convert.ToString(Math.Floor(float.Parse(time)));
            Focus newFocus = new Focus();
            newFocus.rate = 1;
            newFocus.usr = usr;
            newFocus.id = id;

            var emotion = new Dictionary<string, float>();
            emotion.Add("anger", float.Parse(anger));
            emotion.Add("disgust", float.Parse(disgust));
            emotion.Add("fear", float.Parse(fear));
            emotion.Add("happiness", float.Parse(happiness));
            emotion.Add("neutral", float.Parse(neutral));
            emotion.Add("sadness", float.Parse(sadness));
            emotion.Add("surprise", float.Parse(surprise));
            emotion.Add("vector_x", Math.Abs(float.Parse(vector_x)));
            emotion.Add("vector_y", Math.Abs(float.Parse(vector_y)));
            emotion.Add("vector_z", Math.Abs(float.Parse(vector_z)));
            emotion.Add("position_x", float.Parse(position_x));
            emotion.Add("position_y", float.Parse(position_y));

            Focus result = _focusService.GetOne(id, usr);
            if(result == null)
            {
                var document = new Dictionary<string, Dictionary<string, float>>();
                document.Add(cTime, emotion);
                newFocus.emotion = document;
                _focusService.Create(newFocus);
            }
            else
            {
                result.emotion[cTime] = emotion;
                _focusService.Update(id, usr, result);
            }

            return "Success!";
        }

        [Route("get")]
        [HttpGet]
        public JsonResult GetFocus([FromQuery] string usr, [FromQuery] string id)
        {
            var result = _focusService.GetOne(id, usr);
            if(result != null)
            {
                var jsonBody = new Dictionary<int, float>();
                for (int i = 0; i < 600; i++)
                {
                    if (result.emotion.ContainsKey(Convert.ToString(i)))
                    {
                        jsonBody.Add(i, calcuFocus(result.emotion[Convert.ToString(i)]));
                    }
                }
                return new JsonResult(jsonBody);
            }
            else
            {
                return new JsonResult("None");
            }
        }

        [Route("getavg")]
        [HttpGet]
        public JsonResult GetAvgFocus([FromQuery] string id)
        {
            var result = _focusService.GetAll(id);
            if(result != null)
            {
                var jsonBody = new Dictionary<int, float>();
                float allweight = 0;
                foreach (var focus in result)
                {
                    float weight = focus.rate;
                    allweight += weight;
                    for (int i = 0; i < 600; i++)
                    {
                        if (focus.emotion.ContainsKey(Convert.ToString(i)))
                        {
                            if (jsonBody.ContainsKey(i))
                            {
                                jsonBody[i] += calcuFocus(focus.emotion[Convert.ToString(i)]) * weight;
                            }
                            else
                            {
                                jsonBody.Add(i, calcuFocus(focus.emotion[Convert.ToString(i)])*weight);
                            }
                        }
                    }
                }
                for(int i = 0; i < 600; i++)
                {
                    if (jsonBody.ContainsKey(i))
                    {
                        jsonBody[i] /= allweight;
                    }
                }
                return new JsonResult(jsonBody);
            }
            else
            {
                return new JsonResult("None");
            }
        }

        [Route("rate")]
        [HttpGet]
        public ActionResult<string> Rate([FromQuery] string usr, [FromQuery] string id, [FromQuery] string rate)
        {
            var result = _focusService.GetOne(id, usr);
            if(result != null)
            {
                result.rate = float.Parse(rate) / 5;
                _focusService.Update(id, usr, result);
            }
            return "Success!";
        }
    }
}
