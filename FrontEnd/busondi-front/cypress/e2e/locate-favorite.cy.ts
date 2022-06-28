describe('Search favorite line departure time', () => {
    it('Visits the home page with an logged user', () => {
        cy.visit('/')
        cy.contains('Localize seus ônibus de forma prática')
        cy.contains('Salve e acesse facilmente suas linhas favoritas')
      })
    
      it('Log in', () => {
        cy.get('[data-cy=login]').click()
        cy.get('[data-cy=email_login]').type('arthur@ufmg.teste')
        cy.get('[data-cy=password_login]').type('1234')
        cy.get('[data-cy=login_request]').click()
        cy.wait(1000)
    })

    it('Visits the line location page', () => {
        cy.get('[data-cy=menu]').click()
        cy.wait(1000)
        cy.get('[data-cy=locate-line]').click()
        cy.get('[data-cy=menu]').click()
      });
    
      it('Fetch the line departure time and save the request as favorite', () => {
        cy.get('[data-cy=line]').type("5203")
        cy.contains('5203 - Castelo/Estrela Do Oriente-Via Manacas (Principal)').click()
        cy.get('[data-cy=departure]').type("Rua")
        cy.contains('Rua Das Canoas 955').click()
        cy.get('[data-cy=save]').click()
        cy.wait(1000)
        cy.get('[data-cy=submit]').click()
      });

      it('Checks the location result page', () => {
        cy.contains('O próximo ônibus da linha 5203 chegará no ponto de partida às')
        cy.wait(1000)
      })

      it('Go to home and check favorites then log out', () => {
        cy.get('[data-cy=menu]').click()
        cy.get('[data-cy=home]').click()
        cy.get('[data-cy=menu]').click()
        cy.contains('5203 - Rua Das Canoas 955')
        cy.wait(2000)
        cy.get('[data-cy=logout]').click()
        cy.wait(1000)
    })

    it('Log in again', () => {
        cy.get('[data-cy=login]').click()
        cy.get('[data-cy=email_login]').type('arthur@ufmg.teste')
        cy.get('[data-cy=password_login]').type('1234')
        cy.get('[data-cy=login_request]').click()
        cy.wait(1000)
    })

    it('check departure time of the favorite line', () => {
        cy.wait(1000)
        cy.contains('5203 - Rua Das Canoas 955').click()
    })

    it('Checks the location result page', () => {
        cy.contains('O próximo ônibus da linha 5203 chegará no ponto de partida às')
        cy.wait(1000)
    })

    it('Go to home and remove favorite', () => {
        cy.get('[data-cy=menu]').click()
        cy.get('[data-cy=home]').click()
        cy.get('[data-cy=menu]').click()
        cy.wait(1000)
        cy.get('[data-cy=remove]').click({ multiple: true})
    })

});