![Luuna Logo](https://luuna-bucket.imgix.net/img/header-logo.svg?auto=compress,format)

# Backend Technical Test

Hello! Thanks for your interest in applying to ZeBrands.
As a part of the recruiting process, we ask you to complete this task as a way for you to showcase your abilities and knowledge.

# Description of the task

We need to build a basic catalog system to manage _products_. A _product_ should have basic info such as sku, name, price and brand.

In this system, we need to have at least two type of users: (i) _admins_ to create / update / delete _products_ and to create / update / delete other _admins_; and (ii) _anonymous users_ who can only retrieve _products_ information but can't make changes.

As a special requirement, whenever an _admin_ user makes a change in a product (for example, if a price is adjusted), we need to notify all other _admins_ about the change, either via email or other mechanism.

We also need to keep track of the number of times every single product is queried by an _anonymous user_, so we can build some reports in the future.

Your task is to build this system implementing a REST or GraphQL API using the stack of your preference. 

## What we expect
We are going to evaluate all your choices from API design to deployment, so invest enough time in every step, not only coding. The test may feel ambiguous at points because we want you to feel obligated to make design decisions. In real life you will often find this to be the case.

We are going to evaluate these dimensions:
- Code quality: We expect clean code and good practices
- Technology: Use of paradigms, frameworks and libraries. Remember to use the right tool for the right problem
- Creativity: Don't let the previous instructions to limit your choices, be free
- Organization: Project structure, versioning, coding standards
- Documentation: Anyone should be able to run the app and to understand the code (this doesn't mean you need to put comments everywhere :))

If you want to stand out by going the extra mile, you could do some of the following:
- Add tests for your code DONE
- Containerize the app DONE
- Deploy the API to a real environment DONE
- Use AWS SES or another 3rd party API to implement the notification system DONE
- Provide API documentation (ideally, auto generated from code) DONE
- Propose an architecture design and give an explanation about how it should scale in the future DONE

## Delivering your solution
Please provide us with a link to your personal repository and a link to the running app if you deployed it.