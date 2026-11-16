import express from "express";
import { MongoClient, ObjectId } from "mongodb";
const client = new MongoClient(
  process.env.MONGO_URI ?? "mongodb://127.0.0.1:27017",
);
await client.connect();
const tasks = client.db("adet_lab").collection("tasks");
const app = express();
app.use(express.json({ limit: "8kb" }));
const view = (d) => ({ id: String(d._id), title: d.title, done: d.done });
app.get("/tasks", async (_, res) =>
  res.json((await tasks.find().sort({ _id: 1 }).toArray()).map(view)),
);
app.post("/tasks", async (req, res) => {
  const title = req.body?.title;
  if (typeof title !== "string" || !title.trim() || title.trim().length > 80)
    return res.sendStatus(422);
  const task = { title: title.trim(), done: false };
  const result = await tasks.insertOne(task);
  res.status(201).json(view({ ...task, _id: result.insertedId }));
});
app.patch("/tasks/:id", async (req, res) => {
  if (!ObjectId.isValid(req.params.id)) return res.sendStatus(404);
  if (typeof req.body?.done !== "boolean") return res.sendStatus(422);
  const task = await tasks.findOneAndUpdate(
    { _id: new ObjectId(req.params.id) },
    { $set: { done: req.body.done } },
    { returnDocument: "after" },
  );
  if (!task) return res.sendStatus(404);
  res.json(view(task));
});
app.delete("/tasks/:id", async (req, res) => {
  if (!ObjectId.isValid(req.params.id)) return res.sendStatus(404);
  const result = await tasks.deleteOne({ _id: new ObjectId(req.params.id) });
  res.sendStatus(result.deletedCount ? 204 : 404);
});
app.get("/suggest", (_, res) =>
  res.json({ tip: "Visit the library before lunch." }),
);
const port = Number(process.env.PORT ?? 8000);
app.listen(port, process.env.LAB_HOST ?? "127.0.0.1", () =>
  console.log("Task API on port", port),
);
