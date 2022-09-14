import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AddTutorialComponent } from './components/add-tutorial/add-tutorial.component';
import { Query1Component } from './components/query1/query1.component';
import { CommonModule } from '@angular/common';
import { Query2Component } from './components/query2/query2.component';
import {NgChartsModule} from "ng2-charts";
import {HttpClientModule} from "@angular/common/http";
import { Query3Component } from './components/query3/query3.component';
import { Query4Component } from './components/query4/query4.component';
import { Query5Component } from './components/query5/query5.component';

@NgModule({
  declarations: [
    AppComponent,
    AddTutorialComponent,
    Query1Component,
    Query2Component,
    Query3Component,
    Query4Component,
    Query5Component
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    CommonModule,
    NgChartsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
