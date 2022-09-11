import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

const baseUrl = "http://127.0.0.1:5000/api"

@Injectable({
  providedIn: 'root'
})
export class QueriesService {

  constructor(private http: HttpClient) { }

  getQuery1(): Observable<any>{
    return this.http.get<any>(`${baseUrl}/q1`);
  }getQuery2(): Observable<any>{
    return this.http.get<any>(`${baseUrl}/q2`);
  }getQuery3(): Observable<any>{
    return this.http.get<any>(`${baseUrl}/q3`);
  }getQuery4(): Observable<any>{
    return this.http.get<any>(`${baseUrl}/q4`);
  }getQuery5(): Observable<any>{
    return this.http.get<any>(`${baseUrl}/q5`);
  }getQuery6(): Observable<any>{
    return this.http.get<any>(`${baseUrl}/q6`);
  }getQuery7(): Observable<any>{
    return this.http.get<any>(`${baseUrl}/q7`);
  }getQuery8(): Observable<any>{
    return this.http.get<any>(`${baseUrl}/q8`);
  }getQuery9(): Observable<any>{
    return this.http.get<any>(`${baseUrl}/q9`);
  }getQuery10(): Observable<any>{
    return this.http.get<any>(`${baseUrl}/q10`);
  }

  // getQuery2(): Observable<any>{
  //   return this.http.get<any>(`${baseUrl}/query2`);
  // }

}
