using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;
using System.Collections.Generic;

namespace aita.Models
{
    public class Course
    {
        [BsonId]
        [BsonRepresentation(BsonType.ObjectId)]
        public string _id { get; set; }

        [BsonElement("genre")]
        public string genre { get; set; }

        [BsonElement("title")]
        public string title { get; set; }

        [BsonElement("exam")]
        public string exam { get; set; }

        [BsonElement("time")]
        public string time { get; set; }

        [BsonElement("teacher")]
        public string teacher { get; set; }

        [BsonElement("video")]
        public string video { get; set; }

        [BsonElement("article")]
        public string article { get; set; }

        [BsonElement("date")]
        public string date { get; set; }

        [BsonElement("id")]
        public string id { get; set; }

        [BsonElement("view")]
        public string view { get; set; }

        public Dictionary<string, string> ToDic()
        {
            var result = new Dictionary<string, string>();
            result.Add("id", id);
            result.Add("view", view);
            result.Add("date", date);
            result.Add("article", article);
            result.Add("video", video);
            result.Add("teacher", teacher);
            result.Add("time", time);
            result.Add("title", title);
            result.Add("exam", exam);
            result.Add("genre", genre);

            return result;
        }
    }
}
