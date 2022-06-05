import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FavoriteLineComponent } from './favorite-line.component';

describe('FavoriteLineComponent', () => {
  let component: FavoriteLineComponent;
  let fixture: ComponentFixture<FavoriteLineComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ FavoriteLineComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(FavoriteLineComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
