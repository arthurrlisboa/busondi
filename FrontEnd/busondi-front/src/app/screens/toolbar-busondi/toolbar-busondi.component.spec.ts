import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ToolbarBusondiComponent } from './toolbar-busondi.component';

describe('ToolbarUnloggedComponent', () => {
  let component: ToolbarBusondiComponent;
  let fixture: ComponentFixture<ToolbarBusondiComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ToolbarBusondiComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ToolbarBusondiComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
