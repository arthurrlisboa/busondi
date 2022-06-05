import { TestBed } from '@angular/core/testing';

import { LocalizarLinhaService } from './localizar-linha.service';

describe('LocalizarLinhaService', () => {
  let service: LocalizarLinhaService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(LocalizarLinhaService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
