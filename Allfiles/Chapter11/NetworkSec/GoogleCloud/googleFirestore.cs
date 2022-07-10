// Example of initializing an instance of Firestore
FirestoreDb db = FirestoreDb.Create(project);
Console.WriteLine("Created client with project ID: {0}", project);

// Adding data in a document stored in a collection
DocumentReference doc = db.Collection("customers").Document("cceb");
Dictionary<string, object> customer = new Dictionary<string, object>
{
    { "First", "David" },
    { "Last", "Santana" }

};
await docRef.SetAsync(customer);