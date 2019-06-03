using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

namespace aita.Models
{
    public class Comment
    {
        [BsonElement("id")]
        public string id { get; set; }

        [BsonElement("startTime")]
        public string startTime { get; set; }

        [BsonElement("endTime")]
        public string endTime { get; set; }

        [BsonElement("content")]
        public string content { get; set; }
    }
}
