'use strict';

var gulp = require("gulp"),
    babelify = require('babelify'),
    browserify = require("browserify"),
    connect = require("gulp-connect"),
    source = require("vinyl-source-stream"),
    sass = require('gulp-sass'),
    csso = require('gulp-csso'),
    rename = require('gulp-rename')
;
    
// Main Stylesheet Task
gulp.task('stylesheet', function () {
  return gulp.src('./scss/style.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(csso())
    .pipe(rename('style.css'))
    .pipe(gulp.dest('./build'));
});

// Main Javascript Task
gulp.task('javascript', function() {
   return browserify({
        entries: ["./js/main.js"]
    })
    .transform(babelify.configure({
        presets : ["es2015"]
    }))
    .bundle()
    .pipe(source("bundle.js"))
    .pipe(gulp.dest("./build"))
  ;
});

// Admin Stylesheet Task
gulp.task('admin-stylesheet', function () {
  return gulp.src('./scss/admin/admin.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(csso())
    .pipe(rename('admin.css'))
    .pipe(gulp.dest('./build/admin'));
});

// Admin Javascript Task
gulp.task('admin-javascript', function() {
   return browserify({
        entries: ["./js/admin/admin.js"]
    })
    .transform(babelify.configure({
        presets : ["es2015"]
    }))
    .bundle()
    .pipe(source("bundle.js"))
    .pipe(gulp.dest("./build/admin"))
  ;
});

// watch tasks
gulp.task('watch', function() {
  gulp.watch('./scss/**/*.scss', ['stylesheet']);
  gulp.watch('./js/**/*.js', ['javascript']);
 gulp.watch('./scss/admin/**/*.scss', ['admin-stylesheet']);
  gulp.watch('./js/admin/**/*.js', ['admin-javascript']);

});

// build task
gulp.task('build', ['stylesheet','javascript','admin-stylesheet','admin-javascript']);

// default task
gulp.task('default', ['build', 'watch']);
