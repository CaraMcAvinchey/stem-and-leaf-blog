---
name: 'TEST CASE:'
about: This is a default test case template.
title: ''
labels: ''
assignees: ''

---

_As a site owner, I want to collect payment for sittings so I do not have to deal with checks or cash collections for my services._

## Acceptance Criteria
**Scenario:** 
Given I am on the Stripe Dashboard 
When the customer makes a payment 
Then I should see a successful payment displayed

URL: https://purrfect-sitters-service.herokuapp.com/checkout/105/

## Test Data
4000 0025 0000 3155 0424 242 42424

## Expected Outcome
- [X] Checkout saved to the database and is linked to booking.
- [X] Stripe picks up the payment
