using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

namespace aita.Models
{
    public class Course
    {
        [BsonElement("genre")]
        public string genre { get; set; }

        [BsonElement("tile")]
        public string tile { get; set; }

        [BsonElement("exam")]
        public string exam { get; set; }

        [BsonElement("time")]
        public string time { get; set; }

        [BsonElement("teacher")]
        public string usr { get; set; }

        [BsonElement("video")]
        public string video { get; set; }

        [BsonElement("article")]
        public string article { get; set; }

        [BsonElement("date")]
        public string date { get; set; }

        [BsonElement("id")]
        public string id { get; set; }

        [BsonElement("view")]
        public int view { get; set; }
    }
}
