describe('Search line departure time', () => {
    it('Visits the home page with an logged user', () => {
      cy.visit('/')
      cy.contains('Localize seus ônibus de forma prática')
      cy.contains('Salve e acesse facilmente suas linhas favoritas')
    })

    it('Try to log in wile not having a active register', () => {
        cy.get('[data-cy=login]').click()
        cy.get('[data-cy=email_login]').type('arthur@ufmg.teste')
        cy.get('[data-cy=password_login]').type('1234')
        cy.get('[data-cy=login_request]').click()
        cy.get('[data-cy=login-error]').click()
        cy.get('[data-cy=register]').click()
        cy.wait(2000)
    })

    it('Create a new acount', () => {
        cy.get('[data-cy=name]').type('arthur')
        cy.get('[data-cy=email]').type('arthur@ufmg.teste')
        cy.get('[data-cy=password]').type('1234')
        cy.get('[data-cy=register_request]').click()
        cy.wait(1000)
        cy.get('[data-cy=register_ok]').click()
    })

    it('Log in', () => {
        cy.get('[data-cy=email_login]').type('arthur@ufmg.teste')
        cy.get('[data-cy=password_login]').type('1234')
        cy.get('[data-cy=login_request]').click()
        cy.wait(1000)
    })
  
    it('Visits the line location page', () => {
      cy.get('[data-cy=menu]').click()
      cy.get('[data-cy=locate-line]').click()
      cy.get('[data-cy=menu]').click()
    });
  
    it('Fetch the line departure time and save the request as favorite', () => {
      cy.get('[data-cy=line]').type("1404")
      cy.contains('1404A - Palmeiras / Alipio De Melo (Principal)').click()
      cy.get('[data-cy=departure]').type("Rua")
      cy.contains('Rua Curitiba 656').click()
      cy.get('[data-cy=save]').click()
      cy.wait(1000)
      cy.get('[data-cy=submit]').click()
    });
  
    it('Checks the location result page', () => {
      cy.contains('O próximo ônibus da linha 1404A chegará no ponto de partida às')
      cy.wait(1000)
    })
  
    it('Go to home and check favorites', () => {
        cy.get('[data-cy=menu]').click()
        cy.get('[data-cy=home]').click()
        cy.get('[data-cy=menu]').click()
        cy.contains('1404A - Rua Curitiba 656')
        cy.wait(2000)
        cy.get('[data-cy=remove]').click({ multiple: true})
    })
  
  });