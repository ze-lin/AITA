using aita.Models;
using Microsoft.Extensions.Configuration;
using MongoDB.Driver;
using System.Collections.Generic;

namespace aita.Services
{
    public class FocusService
    {
        private readonly IMongoCollection<Focus> _focuses;

        public FocusService(IConfiguration config)
        {
            var client = new MongoClient(config.GetConnectionString("aita"));
            var database = client.GetDatabase("aita");
            _focuses = database.GetCollection<Focus>("focus");
        }

        public List<Focus> GetAll(string id)
        {
            return _focuses.Find(focus => focus.id == id).ToList();
        }

        public Focus GetOne(string id, string usr)
        {
            return _focuses.Find<Focus>(focus => focus.id == id && focus.usr ==usr).FirstOrDefault();
        }

        public void Create(Focus newFocus)
        {
            _focuses.InsertOne(newFocus);
        }

        public void Update(string id, string usr, Focus newFocus)
        {
            _focuses.ReplaceOne(focus => focus.id == id && focus.usr == usr, newFocus);
        }
    }
}
