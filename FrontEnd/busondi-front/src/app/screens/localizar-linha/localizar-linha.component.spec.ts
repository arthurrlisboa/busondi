import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LocalizarLinhaComponent } from './localizar-linha.component';

describe('LocalizarLinhaComponent', () => {
  let component: LocalizarLinhaComponent;
  let fixture: ComponentFixture<LocalizarLinhaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LocalizarLinhaComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(LocalizarLinhaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
