import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LocalizacaoLinhaComponent } from './localizacao-linha.component';

describe('LocalizacaoLinhaComponent', () => {
  let component: LocalizacaoLinhaComponent;
  let fixture: ComponentFixture<LocalizacaoLinhaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LocalizacaoLinhaComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(LocalizacaoLinhaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
