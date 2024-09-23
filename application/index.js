const mongoose = require('mongoose')
const express = require('express')
const app = express()
const port = 4000

app.use(express.json())

// example local uri: mongodb://localhost:27017/devops-e2e
// example docker uri: mongodb://yourUsername:yourPassword@localhost:27017/devops-e2e?authSource=admin

mongoose.connect(process.env.MONGO_URI)
    .then(() => {
        console.log('Connected to MongoDB');
    })
    .catch((err) => {
        console.error('Error connecting to MongoDB:', err);
    });

const userSchema = new mongoose.Schema({
    name: String,
    age: Number,
});

const User = mongoose.model('User', userSchema);

app.get('/', async (request, response) => {
    await User.find()
        .then((users) => {
            response.json({ 'Users': users });
        })
        .catch((err) => {
            response.json({ 'Error fetch users': err });
        });
})

app.post('/', (request, response) => {
    const { name, age } = request.body;

    const newUser = new User({ name, age });

    newUser.save()
        .then((user) => {
            response.json({ 'User saved': user });
        })
        .catch((err) => {
            response.json({ 'Error saving user': err });
        });
})

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
})