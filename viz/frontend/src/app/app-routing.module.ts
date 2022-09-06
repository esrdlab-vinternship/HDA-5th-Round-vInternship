import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {AddTutorialComponent} from "./components/add-tutorial/add-tutorial.component";
import {Query1Component} from "./components/query1/query1.component";
import {Query2Component} from "./components/query2/query2.component";
import {Query3Component} from "./components/query3/query3.component";

const routes: Routes = [
  {path: 'first-component', component: AddTutorialComponent},
  {path: 'query1', component: Query1Component},
  {path: 'query2', component: Query2Component},
  {path: 'query3', component: Query3Component},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}
