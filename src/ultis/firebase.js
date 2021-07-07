import firebase from "firebase/app";
import "firebase/firestore";
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDF9BIm_uRHiNWL34u2ZrFO2hQLKk12ktA",
  authDomain: "dictionary-chinese-22347.firebaseapp.com",
  projectId: "dictionary-chinese-22347",
  storageBucket: "dictionary-chinese-22347.appspot.com",
  messagingSenderId: "78285852020",
  appId: "1:78285852020:web:bf2d72fac1a6c1f4433021",
  measurementId: "G-V818KMTMET",
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
const db = firebase.firestore();

export default db;
