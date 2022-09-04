import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {AddCommandModule} from "@angular/cli/src/commands/add/cli";
import {AddTutorialComponent} from "./components/add-tutorial/add-tutorial.component";

const routes: Routes = [
  { path: 'first-component', component: AddTutorialComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
