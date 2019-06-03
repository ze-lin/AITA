using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

namespace aita.Models
{
    public class Collection
    {
        [BsonElement("id")]
        public string id { get; set; }

        [BsonElement("usr")]
        public string usr { get; set; }
    }
}
