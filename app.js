const express = require('express');
const bodyParser = require('body-parser');
const app = express();

app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({ extended: true }));

app.use(express.static('public'));

app.get('/', (req, res) => {
  res.render('index');
});

app.get('/calculator', (req, res) => {
  res.render('calculatorOptions');
});

app.post('/calculator', (req, res) => {

  const calculatorOption = req.body.calculatorOption;
  if (calculatorOption === 'SimpleInterest') {
    res.redirect('/calculator/SimpleInterest');
  } else if (calculatorOption === 'CompoundInterest') {
    res.redirect('/calculator/CompoundInterest');
  } else {
    res.redirect('/calculator');
  }
});

app.get('/calculator/SimpleInterest', (req, res) => {
  res.render('SimpleInterest', { result: null });
});

app.get('/calculator/CompoundInterest', (req, res) => {
  res.render('CompoundInterest', { result: null });
});

app.post('/calculator/SimpleInterest', (req, res) => {
  const principal = parseFloat(req.body.principal);
  const rate = parseFloat(req.body.rate) / 100; 
  const time = parseFloat(req.body.time);

  const SimpleInterest = (principal * rate * time).toFixed(2);

  res.render('SimpleInterest', { result: { SimpleInterest } });
});

app.post('/calculator/CompoundInterest', (req, res) => {
  const principal = parseFloat(req.body.principal);
  const rate = parseFloat(req.body.rate) / 100; 
  const time = parseFloat(req.body.time) / 12;
  const n = parseInt(req.body.n);

  const CompoundInterest = ((principal * (((1+(rate/n))**(n*time)).toFixed(6)))-principal).toFixed(2);
  
  res.render('CompoundInterest', { result: { CompoundInterest } });
  
});

const port = 3000;
app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});