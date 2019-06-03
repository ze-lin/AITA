using System.Collections.Generic;
using aita.Models;
using Microsoft.Extensions.Configuration;
using MongoDB.Driver;


namespace aita.Services
{
    public class CommentService
    {
        private readonly IMongoCollection<Comment> _comments;

        public CommentService(IConfiguration config)
        {
            var client = new MongoClient(config.GetConnectionString("aita"));
            var database = client.GetDatabase("aita");
            _comments = database.GetCollection<Comment>("comment");
        }

        public List<Comment> GetAll(string id)
        {
            return _comments.Find(comment => comment.id == id).ToList();
        }

        public void Create(Comment newComment)
        {
            _comments.InsertOne(newComment);
        }
    }
}
