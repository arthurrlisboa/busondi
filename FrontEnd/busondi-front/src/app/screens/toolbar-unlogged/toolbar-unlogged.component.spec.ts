import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ToolbarUnloggedComponent } from './toolbar-unlogged.component';

describe('ToolbarUnloggedComponent', () => {
  let component: ToolbarUnloggedComponent;
  let fixture: ComponentFixture<ToolbarUnloggedComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ToolbarUnloggedComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ToolbarUnloggedComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
