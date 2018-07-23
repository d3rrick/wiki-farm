import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
// import {environment} from "../../environment/environment"


@Injectable({
  providedIn: 'root'
})
export class SearchService {
  weatherInfo:any;
  loading:boolean
  constructor(private http:HttpClient) {
    
   }

   getWeather(){
     let url ="http://20.20.22.71:5000/weather/?long=36.86&lat=-1.25"
     let myPromise= new Promise((resolve,reject)=>
       this.http.get(url).toPromise().then(
        response =>{
          this.weatherInfo=response
          console.log(response)
          resolve()
        },
        error =>{
          console.log(error)
          reject()
        }
       )
     )
     return myPromise
   }
}


class Crop(base):

