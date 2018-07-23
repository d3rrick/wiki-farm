import { Component,OnInit } from '@angular/core';
import {SearchService} from './services/search.service';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [SearchService]
})
export class AppComponent {
  title = 'app';
  loading:boolean
  constructor( private search:SearchService){
    this.loading=false
  }
  getData(){
    this.loading=true
    this.search.getWeather().then(() => this.loading=false);
  }
  ngOninit(){
    this.loading=true
    this.search.getWeather().then(() => this.loading=false);
  }
}
