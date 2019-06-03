using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;
using System.Collections.Generic;

namespace aita.Models
{
    public class Focus
    {
        [BsonId]
        [BsonRepresentation(BsonType.ObjectId)]
        public string _id { get; set; }

        [BsonElement("usr")]
        public string usr { get; set; }

        [BsonElement("id")]
        public string id { get; set; }

        [BsonElement("rate")]
        public float rate { get; set; }

        [BsonElement("emotion")]
        public Dictionary<string, Dictionary<string, float>> emotion { get; set; } // how to deal with this data object???
    }
}
