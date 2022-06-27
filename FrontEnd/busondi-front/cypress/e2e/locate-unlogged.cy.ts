
describe('Search line departure time', () => {
  it('Visits the home page with an unlogged user', () => {
    cy.visit('/')
    cy.contains('Localize seus ônibus de forma prática')
    cy.contains('Salve e acesse facilmente suas linhas favoritas')
  })

  it('Visits the line location page', () => {
    cy.get('[data-cy=menu]').click()
    cy.get('[data-cy=locate-line]').click()
    cy.get('[data-cy=menu]').click()
  });

  it('Fetch the the line departure time', () => {
    cy.get('[data-cy=line]').type("1404")
    cy.contains('1404A - Palmeiras / Alipio De Melo (Principal)').click()
    cy.get('[data-cy=departure]').type("Rua")
    cy.contains('Rua Curitiba 656').click();
    cy.get('[data-cy=submit]').click()
  });

  it('Checks the location result page', () => {
    cy.contains('O próximo ônibus da linha 1404A chegará no ponto de partida às')
  })

  it('Updates location request with other departure', () => {
    cy.get('[data-cy=departure]').clear().type("Rua")
    cy.contains('Curitiba 862').click();
    cy.get('[data-cy=submit]').click();
    cy.contains('O próximo ônibus da linha 1404A chegará no ponto de partida às')
  })

});
