using aita.Models;
using Microsoft.Extensions.Configuration;
using MongoDB.Driver;
using System.Collections.Generic;

namespace aita.Services
{
    public class CompleteService
    {
        private readonly IMongoCollection<Collection> _collections;
        private readonly IMongoCollection<Course> _courses;
        private readonly IMongoCollection<Focus> _focuses;

        public CompleteService(IConfiguration config)
        {
            var client = new MongoClient(config.GetConnectionString("aita"));
            var database = client.GetDatabase("aita");
            _collections = database.GetCollection<Collection>("collection");
            _courses = database.GetCollection<Course>("course");
            _focuses = database.GetCollection<Focus>("focus");
        }

        public List<Collection> GetAll(string usr)
        {
            return _collections.Find(collection => collection.usr == usr).ToList();
        }

        public Focus GetFocus(string id, string usr)
        {
            return _focuses.Find(focus => focus.id == id && focus.usr == usr).FirstOrDefault();
        }

        public Course GetCourse(string id)
        {
            return _courses.Find(course => course.id == id).FirstOrDefault();
        }
    }
}
