// const cypress = require("cypress")


describe('Download A Subtitle', () => {
 /* it('Connexion à Spotify!', () => {
    cy.visit("https://www.spotify.com/");

    cy.get('.mh-mobile-menu')
    .get('nav > ul > :nth-child(6)').click();

    cy.get('#login-username').type("rami2****@outlook.fr {enter}");

    cy.get("#login-password").type("********{enter}");

    cy.get(".Button-sc-1dqy6lx-0").click();

    cy.get(".RSg3qFREWrqWCuUvDpJR > :nth-child(2) > a > span").click();
  });
 */

  it('Open and download Ingrid goes west subtitle!', () => {
    cy.visit("https://www.subscene.com/");

    cy.get('form > :nth-child(1)').type('ingrid goes west{enter}');
    cy.contains('Ingrid Goes West (2017)').click();
    cy.get('a').eq(20).click();
    cy.get('.clearfix > :nth-child(1) > a').click();
    //cy.get('a').click(['multiple: true']);
    
  });
})
/*
describe('Librairie AlKitab Test', () => {
    it('Add Book To Cart!', () => {
      cy.visit("https://www.alkitab.tn/");

      cy.get(':nth-child(1) > .quiz-title > .h-link').click();

      
      cy.contains("Quiz HTML débutant").should('be.visible');

      cy.get('#q0r2').click();
      cy.get('#q1r2').click();
      cy.get('#q2r4').click();
      cy.get('#q3r1').click(); 
      cy.get('#q4r6').click();
      cy.get('#q5r1').click();
      cy.get('#q6r5').click();
      cy.get('#q7r3').click();
      cy.get('#q8r2').click();
      cy.get('#q9r1').click();


      cy.get('.center > .awesome').click();

      cy.get('.quiz-score-value').invoke("text").should("eq", "10/10");
    })
  })
*/