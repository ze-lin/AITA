using aita.Models;
using Microsoft.Extensions.Configuration;
using MongoDB.Driver;

namespace aita.Services
{
    public class MemberService
    {
        private readonly IMongoCollection<Member> _members;

        public MemberService(IConfiguration config)
        {
            var client = new MongoClient(config.GetConnectionString("aita"));
            var database = client.GetDatabase("aita");
            _members = database.GetCollection<Member>("member");
        }

        public Member Get(string usr)
        {
            return _members.Find<Member>(member => member.usr == usr).FirstOrDefault();
        }

        public void Create (Member member)
        {
            _members.InsertOne(member);
        }

        public void Update(string usr, Member newMember)
        {
            _members.ReplaceOne(member => member.usr == usr, newMember);
        }
    }
}
