---
layout: default
title: Contact
---

# Contact Me

<div style="text-align: center; margin: 20px 0;">
  <img src="assets/img/dae-logo.svg" alt="dae Logo" style="height: 50px;">
</div>

## Get In Touch

I'm always open to discussing new projects, creative ideas, or opportunities to be part of your vision.

<div class="contact-methods">
  <div class="contact-method">
    <h3>Email</h3>
    <p><a href="mailto:matt.johnson@example.com">matt.johnson@example.com</a></p>
  </div>
  
  <div class="contact-method">
    <h3>LinkedIn</h3>
    <p><a href="https://linkedin.com/in/mattjohnson" target="_blank">linkedin.com/in/mattjohnson</a></p>
  </div>
  
  <div class="contact-method">
    <h3>GitHub</h3>
    <p><a href="https://github.com/mattjohnson" target="_blank">github.com/mattjohnson</a></p>
  </div>
</div>

## Contact Form

<form action="https://formspree.io/f/your-form-id" method="POST" class="contact-form">
  <div class="form-group">
    <label for="name">Name</label>
    <input type="text" id="name" name="name" required>
  </div>
  
  <div class="form-group">
    <label for="email">Email</label>
    <input type="email" id="email" name="_replyto" required>
  </div>
  
  <div class="form-group">
    <label for="subject">Subject</label>
    <input type="text" id="subject" name="subject" required>
  </div>
  
  <div class="form-group">
    <label for="message">Message</label>
    <textarea id="message" name="message" rows="5" required></textarea>
  </div>
  
  <button type="submit" class="btn">Send Message</button>
</form>

<style>
  .contact-methods {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    margin: 30px 0;
  }
  
  .contact-method {
    flex-basis: 30%;
    margin-bottom: 20px;
    padding: 15px;
    border: 1px solid #ddd;
    border-radius: 5px;
    text-align: center;
  }
  
  .contact-form {
    max-width: 600px;
    margin: 0 auto;
  }
  
  .form-group {
    margin-bottom: 20px;
  }
  
  .form-group label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
  }
  
  .form-group input,
  .form-group textarea {
    width: 100%;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
  }
  
  .btn {
    display: inline-block;
    padding: 10px 20px;
    background-color: #333;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    text-decoration: none;
  }
  
  .btn:hover {
    background-color: #555;
  }
  
  @media (max-width: 768px) {
    .contact-method {
      flex-basis: 100%;
    }
  }
</style>