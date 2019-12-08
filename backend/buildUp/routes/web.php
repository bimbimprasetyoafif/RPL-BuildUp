<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/


//login
Route::get('/login', 'AuthController@login')->name('login');
Route::post('/postlogin', 'AuthController@postlogin');
Route::get('/logout', 'AuthController@logout');

Route::group(['middleware' => 'auth'], function () {
    Route::get('/', 'PagesController@home');
    Route::get('/products', 'ProductsController@index')->name('products.index');

    //student
    Route::get('/students', 'StudentsController@index');
    Route::get('/students/create', 'StudentsController@create');
    Route::get('/students/{student}', 'StudentsController@show');
    Route::post('/students', 'StudentsController@store');
    Route::delete('/students/{student}', 'StudentsController@destroy');
    Route::get('/students/{student}/edit', 'StudentsController@edit');
    Route::patch('/students/{student}', 'StudentsController@update');
});
