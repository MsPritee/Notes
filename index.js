const express = require("express");
const app = express();
const mongoose = require("mongoose");
const port = 3000;

// Middleware for parsing JSON request bodies
app.use(express.json());

mongoose
  .connect("mongodb://localhost:27017/api_2_db", {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => console.log("MongoDB connected"))
  .catch((err) => console.error("MongoDB connection error:", err));

const userSchema = new mongoose.Schema({
  username: { type: String, required: true, unique: true },
  password: { type: String, required: true },
});

const User = mongoose.model("User", userSchema);

app.post("/register", async (req, res) => {
  const { username, password } = req.body;

  // Basic validation (add more robust validation)
  if (!username || !password) {
    return res.status(400).json({ error: "Username and password required" });
  }

  // Check if user exist
  try {
    const existingUser = await User.findOne({ username });
    if (existingUser) {
      return res.status(409).json({ error: "User already exists" });
    }

    // Create new user
    const newUser = new User({ username, password });
    await newUser.save();
    res.status(201).json({ message: "User registered successfully" });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "An error occurred" });
  }
});


// app.get("/users", (req, res) => {
//   const users = [
//     { id: 1, name: "John Doe" },
//     { id: 2, name: "Jane Smith" },
//   ];
//   res.json(users);
// });


app.get("/users", async (req, res) => {
  try {
    const users = await User.find();
    res.json(users);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "An error occurred" });
  }
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
