using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

namespace aita.Models
{
    public class Focus
    {
        [BsonElement("usr")]
        public string usr { get; set; }

        [BsonElement("id")]
        public string id { get; set; }

        [BsonElement("rate")]
        public int rate { get; set; }

        [BsonElement("emotion")]
        public string emotion { get; set; } // how to deal with this data object???
    }
}
