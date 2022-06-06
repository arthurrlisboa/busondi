import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LocalizacaoRotaComponent } from './localizacao-rota.component';

describe('LocalizacaoRotaComponent', () => {
  let component: LocalizacaoRotaComponent;
  let fixture: ComponentFixture<LocalizacaoRotaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LocalizacaoRotaComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(LocalizacaoRotaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
