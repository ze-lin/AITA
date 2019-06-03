using aita.Models;
using aita.Services;
using Microsoft.AspNetCore.Mvc;

namespace aita.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class ValuesController : ControllerBase
    {
        private readonly MemberService _memberService;

        public ValuesController(MemberService memberService)
        {
            _memberService = memberService;
        }
        // GET api/values
        [HttpGet]
        public ActionResult<string> Get()
        {
            var test = new Member();
            test.usr = "test";
            test.pwd = "123123";
            test.role = "teacher";
            test.pic = "images";
            test.date = "2019";

           //  _memberService.Create(test);

            return "Hello World";
        }

        // GET api/values/5
        [HttpGet("{id}")]
        public ActionResult<string> Get(int id)
        {
            return "value";
        }

        // POST api/values
        [HttpPost]
        public void Post([FromBody] string value)
        {
        }

        // PUT api/values/5
        [HttpPut("{id}")]
        public void Put(int id, [FromBody] string value)
        {
        }

        // DELETE api/values/5
        [HttpDelete("{id}")]
        public void Delete(int id)
        {
        }
    }
}
