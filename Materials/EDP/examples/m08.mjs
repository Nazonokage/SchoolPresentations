import { Subject, of, timer } from 'rxjs';
import { debounceTime, distinctUntilChanged, switchMap, map, catchError, finalize } from 'rxjs/operators';
const terms = new Subject();
const subscription = terms.pipe(
  debounceTime(10),
  distinctUntilChanged(),
  switchMap(term => timer(30).pipe(
    map(() => {
      if (term === 'error') throw new Error('Search unavailable');
      return 'Results: ' + term.toUpperCase();
    }),
    catchError(error => of('Handled: ' + error.message))
  )),
  finalize(() => console.log('Search subscription closed'))
).subscribe(value => console.log(value));
terms.next('c'); terms.next('ca'); terms.next('canteen');
await new Promise(resolve => setTimeout(resolve, 80));
terms.next('error');
await new Promise(resolve => setTimeout(resolve, 80));
subscription.unsubscribe();
terms.complete();
