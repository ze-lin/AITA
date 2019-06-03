using System.Collections.Generic;
using aita.Models;
using Microsoft.Extensions.Configuration;
using MongoDB.Driver;

namespace aita.Services
{
    public class CourseService
    {
        private readonly IMongoCollection<Course> _courses;

        public CourseService(IConfiguration config)
        {
            var client = new MongoClient(config.GetConnectionString("aita"));
            var database = client.GetDatabase("aita");
            _courses = database.GetCollection<Course>("course");
        }

        public List<Course> GetAll()
        {
            return _courses.Find(course => true).ToList();
        }

        public List<Course> GetAll(string teacher)
        {
            return _courses.Find(course => course.teacher == teacher).ToList();
        }

        public Course Get(string id)
        {
            return _courses.Find<Course>(course => course.id == id).FirstOrDefault();
        }

        public void Create(Course course)
        {
            _courses.InsertOne(course);
        }

        public void Delete(string id)
        {
            _courses.DeleteOne(course => course.id == id);
        }

        public void Update(string id, Course newCourse)
        {
            _courses.ReplaceOne(course => course.id == id, newCourse);
        }
    }
}
