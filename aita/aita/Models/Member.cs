using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

namespace aita.Models
{
    public class Member
    {
        [BsonId]
        [BsonRepresentation(BsonType.ObjectId)]
        public string _id { get; set; }

        [BsonElement("usr")]
        public string usr { get; set; }

        [BsonElement("pwd")]
        public string pwd { get; set; }

        [BsonElement("role")]
        public string role { get; set; }

        [BsonElement("date")]
        public string date { get; set; }

        [BsonElement("pic")]
        public string pic { get; set; }
    }
}
