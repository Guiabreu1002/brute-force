<?php

use App\Http\Controllers\BruteForceController;
use Illuminate\Support\Facades\Route;

Route::post('/login', [BruteForceController::class, 'login'])->middleware('throttle:login');
