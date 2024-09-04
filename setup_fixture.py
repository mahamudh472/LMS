import json

data = [
    {
        "model": "auth.user",
        "pk": 100,
        "fields": {
            "username": "admin2",
            "password": "admin",
            "email": "john@example.com",
            "is_staff": True,
            "is_superuser": True
        }
    },{
        "model": "auth.user",
        "pk": 1,
        "fields": {
            "username": "john",
            "password": "pbkdf2_sha256$150000$...$...",
            "email": "john@example.com",
            "is_staff": False,
            "is_superuser": False
        }
    },
    {
        "model": "accounts.studentprofile",
        "pk": 1,
        "fields": {
            "user": 1,
            "shift": "বিকেল",
            "department": "কম্পিউটার বিজ্ঞান",
            "roll": "001",
            "name": "জন ডো",
            "father_name": "রিচার্ড ডো",
            "mother_name": "জেন ডো",
            "address": "১২৩ মেইন স্ট্রিট",
            "post_office": "SomePostOffice",
            "upazila": "SomeUpazila",
            "district": "SomeDistrict",
            "number": "১২৩৪৫৬৭৮৯০",
            "parent_number": "০৯৮৭৬৫৪৩২১",
            "blood_group": "A+",
            "technology_code": "CS001",
            "semester": "১ম",
            "birth_date": "2000-01-01",
            "ssc_roll": "SSC001",
            "image": None,
            "signature": None,
            "parent_signature": None,
            "policy_agreement": True,
            "is_active": False
        }
    },{
        "model": "auth.user",
        "pk": 32,
        "fields": {
            "username": "john_doe1",
            "password": "pbkdf2_sha256$150000$...$...",
            "email": "john@example.com",
            "is_staff": False,
            "is_superuser": False
        }
    },
    {
        "model": "accounts.studentprofile",
        "pk": 32,
        "fields": {
            "user": 32,
            "shift": "বিকেল",
            "department": "কম্পিউটার বিজ্ঞান",
            "roll": "001",
            "name": "জন ডো",
            "father_name": "রিচার্ড ডো",
            "mother_name": "জেন ডো",
            "address": "১২৩ মেইন স্ট্রিট",
            "post_office": "SomePostOffice",
            "upazila": "SomeUpazila",
            "district": "SomeDistrict",
            "number": "১২৩৪৫৬৭৮৯০",
            "parent_number": "০৯৮৭৬৫৪৩২১",
            "blood_group": "A+",
            "technology_code": "CS001",
            "semester": "১ম",
            "birth_date": "2000-01-01",
            "ssc_roll": "SSC001",
            "image": None,
            "signature": None,
            "parent_signature": None,
            "policy_agreement": True,
            "is_active": False
        }
    },{
        "model": "auth.user",
        "pk": 3,
        "fields": {
            "username": "john_doe2",
            "password": "pbkdf2_sha256$150000$...$...",
            "email": "john@example.com",
            "is_staff": False,
            "is_superuser": False
        }
    },
    {
        "model": "accounts.studentprofile",
        "pk": 3,
        "fields": {
            "user": 3,
            "shift": "বিকেল",
            "department": "কম্পিউটার বিজ্ঞান",
            "roll": "001",
            "name": "জন ডো",
            "father_name": "রিচার্ড ডো",
            "mother_name": "জেন ডো",
            "address": "১২৩ মেইন স্ট্রিট",
            "post_office": "SomePostOffice",
            "upazila": "SomeUpazila",
            "district": "SomeDistrict",
            "number": "১২৩৪৫৬৭৮৯০",
            "parent_number": "০৯৮৭৬৫৪৩২১",
            "blood_group": "A+",
            "technology_code": "CS001",
            "semester": "১ম",
            "birth_date": "2000-01-01",
            "ssc_roll": "SSC001",
            "image": None,
            "signature": None,
            "parent_signature": None,
            "policy_agreement": True,
            "is_active": False
        }
    },{
        "model": "auth.user",
        "pk": 4,
        "fields": {
            "username": "john_doe4",
            "password": "pbkdf2_sha256$150000$...$...",
            "email": "john@example.com",
            "is_staff": False,
            "is_superuser": False
        }
    },
    {
        "model": "accounts.studentprofile",
        "pk": 4,
        "fields": {
            "user": 4,
            "shift": "বিকেল",
            "department": "কম্পিউটার বিজ্ঞান",
            "roll": "001",
            "name": "জন ডো",
            "father_name": "রিচার্ড ডো",
            "mother_name": "জেন ডো",
            "address": "১২৩ মেইন স্ট্রিট",
            "post_office": "SomePostOffice",
            "upazila": "SomeUpazila",
            "district": "SomeDistrict",
            "number": "১২৩৪৫৬৭৮৯০",
            "parent_number": "০৯৮৭৬৫৪৩২১",
            "blood_group": "A+",
            "technology_code": "CS001",
            "semester": "১ম",
            "birth_date": "2000-01-01",
            "ssc_roll": "SSC001",
            "image": None,
            "signature": None,
            "parent_signature": None,
            "policy_agreement": True,
            "is_active": False
        }
    },{
        "model": "auth.user",
        "pk": 5,
        "fields": {
            "username": "john_doe5",
            "password": "pbkdf2_sha256$150000$...$...",
            "email": "john@example.com",
            "is_staff": False,
            "is_superuser": False
        }
    },
    {
        "model": "accounts.studentprofile",
        "pk": 5,
        "fields": {
            "user": 5,
            "shift": "বিকেল",
            "department": "কম্পিউটার বিজ্ঞান",
            "roll": "001",
            "name": "জন ডো",
            "father_name": "রিচার্ড ডো",
            "mother_name": "জেন ডো",
            "address": "১২৩ মেইন স্ট্রিট",
            "post_office": "SomePostOffice",
            "upazila": "SomeUpazila",
            "district": "SomeDistrict",
            "number": "১২৩৪৫৬৭৮৯০",
            "parent_number": "০৯৮৭৬৫৪৩২১",
            "blood_group": "A+",
            "technology_code": "CS001",
            "semester": "১ম",
            "birth_date": "2000-01-01",
            "ssc_roll": "SSC001",
            "image": None,
            "signature": None,
            "parent_signature": None,
            "policy_agreement": True,
            "is_active": False
        }
    },{
        "model": "auth.user",
        "pk": 6,
        "fields": {
            "username": "john_doe6",
            "password": "pbkdf2_sha256$150000$...$...",
            "email": "john@example.com",
            "is_staff": False,
            "is_superuser": False
        }
    },
    {
        "model": "accounts.studentprofile",
        "pk": 6,
        "fields": {
            "user": 6,
            "shift": "বিকেল",
            "department": "কম্পিউটার বিজ্ঞান",
            "roll": "001",
            "name": "জন ডো",
            "father_name": "রিচার্ড ডো",
            "mother_name": "জেন ডো",
            "address": "১২৩ মেইন স্ট্রিট",
            "post_office": "SomePostOffice",
            "upazila": "SomeUpazila",
            "district": "SomeDistrict",
            "number": "১২৩৪৫৬৭৮৯০",
            "parent_number": "০৯৮৭৬৫৪৩২১",
            "blood_group": "A+",
            "technology_code": "CS001",
            "semester": "১ম",
            "birth_date": "2000-01-01",
            "ssc_roll": "SSC001",
            "image": None,
            "signature": None,
            "parent_signature": None,
            "policy_agreement": True,
            "is_active": False
        }
    },{
        "model": "auth.user",
        "pk": 7,
        "fields": {
            "username": "john_doe7",
            "password": "pbkdf2_sha256$150000$...$...",
            "email": "john@example.com",
            "is_staff": False,
            "is_superuser": False
        }
    },
    {
        "model": "accounts.studentprofile",
        "pk": 7,
        "fields": {
            "user": 7,
            "shift": "বিকেল",
            "department": "কম্পিউটার বিজ্ঞান",
            "roll": "001",
            "name": "জন ডো",
            "father_name": "রিচার্ড ডো",
            "mother_name": "জেন ডো",
            "address": "১২৩ মেইন স্ট্রিট",
            "post_office": "SomePostOffice",
            "upazila": "SomeUpazila",
            "district": "SomeDistrict",
            "number": "১২৩৪৫৬৭৮৯০",
            "parent_number": "০৯৮৭৬৫৪৩২১",
            "blood_group": "A+",
            "technology_code": "CS001",
            "semester": "১ম",
            "birth_date": "2000-01-01",
            "ssc_roll": "SSC001",
            "image": None,
            "signature": None,
            "parent_signature": None,
            "policy_agreement": True,
            "is_active": False
        }
    },{
        "model": "auth.user",
        "pk": 8,
        "fields": {
            "username": "john_doe8",
            "password": "pbkdf2_sha256$150000$...$...",
            "email": "john@example.com",
            "is_staff": False,
            "is_superuser": False
        }
    },
    {
        "model": "accounts.studentprofile",
        "pk": 8,
        "fields": {
            "user": 8,
            "shift": "বিকেল",
            "department": "কম্পিউটার বিজ্ঞান",
            "roll": "001",
            "name": "জন ডো",
            "father_name": "রিচার্ড ডো",
            "mother_name": "জেন ডো",
            "address": "১২৩ মেইন স্ট্রিট",
            "post_office": "SomePostOffice",
            "upazila": "SomeUpazila",
            "district": "SomeDistrict",
            "number": "১২৩৪৫৬৭৮৯০",
            "parent_number": "০৯৮৭৬৫৪৩২১",
            "blood_group": "A+",
            "technology_code": "CS001",
            "semester": "১ম",
            "birth_date": "2000-01-01",
            "ssc_roll": "SSC001",
            "image": None,
            "signature": None,
            "parent_signature": None,
            "policy_agreement": True,
            "is_active": False
        }
    },{
        "model": "auth.user",
        "pk": 9,
        "fields": {
            "username": "john_doe9",
            "password": "pbkdf2_sha256$150000$...$...",
            "email": "john@example.com",
            "is_staff": False,
            "is_superuser": False
        }
    },
    {
        "model": "accounts.studentprofile",
        "pk": 9,
        "fields": {
            "user": 9,
            "shift": "বিকেল",
            "department": "কম্পিউটার বিজ্ঞান",
            "roll": "001",
            "name": "জন ডো",
            "father_name": "রিচার্ড ডো",
            "mother_name": "জেন ডো",
            "address": "১২৩ মেইন স্ট্রিট",
            "post_office": "SomePostOffice",
            "upazila": "SomeUpazila",
            "district": "SomeDistrict",
            "number": "১২৩৪৫৬৭৮৯০",
            "parent_number": "০৯৮৭৬৫৪৩২১",
            "blood_group": "A+",
            "technology_code": "CS001",
            "semester": "১ম",
            "birth_date": "2000-01-01",
            "ssc_roll": "SSC001",
            "image": None,
            "signature": None,
            "parent_signature": None,
            "policy_agreement": True,
            "is_active": False
        }
    },{
        "model": "auth.user",
        "pk": 10,
        "fields": {
            "username": "john_doe10",
            "password": "pbkdf2_sha256$150000$...$...",
            "email": "john@example.com",
            "is_staff": False,
            "is_superuser": False
        }
    },
    {
        "model": "accounts.studentprofile",
        "pk": 10,
        "fields": {
            "user": 10,
            "shift": "বিকেল",
            "department": "কম্পিউটার বিজ্ঞান",
            "roll": "001",
            "name": "জন ডো",
            "father_name": "রিচার্ড ডো",
            "mother_name": "জেন ডো",
            "address": "১২৩ মেইন স্ট্রিট",
            "post_office": "SomePostOffice",
            "upazila": "SomeUpazila",
            "district": "SomeDistrict",
            "number": "১২৩৪৫৬৭৮৯০",
            "parent_number": "০৯৮৭৬৫৪৩২১",
            "blood_group": "A+",
            "technology_code": "CS001",
            "semester": "১ম",
            "birth_date": "2000-01-01",
            "ssc_roll": "SSC001",
            "image": None,
            "signature": None,
            "parent_signature": None,
            "policy_agreement": True,
            "is_active": False
        }
    },{
        "model": "auth.user",
        "pk": 11,
        "fields": {
            "username": "john_doe11",
            "password": "pbkdf2_sha256$150000$...$...",
            "email": "john@example.com",
            "is_staff": False,
            "is_superuser": False
        }
    },
    {
        "model": "accounts.studentprofile",
        "pk": 11,
        "fields": {
            "user": 11,
            "shift": "বিকেল",
            "department": "কম্পিউটার বিজ্ঞান",
            "roll": "001",
            "name": "জন ডো",
            "father_name": "রিচার্ড ডো",
            "mother_name": "জেন ডো",
            "address": "১২৩ মেইন স্ট্রিট",
            "post_office": "SomePostOffice",
            "upazila": "SomeUpazila",
            "district": "SomeDistrict",
            "number": "১২৩৪৫৬৭৮৯০",
            "parent_number": "০৯৮৭৬৫৪৩২১",
            "blood_group": "A+",
            "technology_code": "CS001",
            "semester": "১ম",
            "birth_date": "2000-01-01",
            "ssc_roll": "SSC001",
            "image": None,
            "signature": None,
            "parent_signature": None,
            "policy_agreement": True,
            "is_active": False
        }
    },{
        "model": "auth.user",
        "pk": 12,
        "fields": {
            "username": "john_doe12",
            "password": "pbkdf2_sha256$150000$...$...",
            "email": "john@example.com",
            "is_staff": False,
            "is_superuser": False
        }
    },
    {
        "model": "accounts.studentprofile",
        "pk": 12,
        "fields": {
            "user": 12,
            "shift": "বিকেল",
            "department": "কম্পিউটার বিজ্ঞান",
            "roll": "001",
            "name": "জন ডো",
            "father_name": "রিচার্ড ডো",
            "mother_name": "জেন ডো",
            "address": "১২৩ মেইন স্ট্রিট",
            "post_office": "SomePostOffice",
            "upazila": "SomeUpazila",
            "district": "SomeDistrict",
            "number": "১২৩৪৫৬৭৮৯০",
            "parent_number": "০৯৮৭৬৫৪৩২১",
            "blood_group": "A+",
            "technology_code": "CS001",
            "semester": "১ম",
            "birth_date": "2000-01-01",
            "ssc_roll": "SSC001",
            "image": None,
            "signature": None,
            "parent_signature": None,
            "policy_agreement": True,
            "is_active": False
        }
    },{
        "model": "auth.user",
        "pk": 13,
        "fields": {
            "username": "john_doe13",
            "password": "pbkdf2_sha256$150000$...$...",
            "email": "john@example.com",
            "is_staff": False,
            "is_superuser": False
        }
    },
    {
        "model": "accounts.studentprofile",
        "pk": 13,
        "fields": {
            "user": 13,
            "shift": "বিকেল",
            "department": "কম্পিউটার বিজ্ঞান",
            "roll": "001",
            "name": "জন ডো",
            "father_name": "রিচার্ড ডো",
            "mother_name": "জেন ডো",
            "address": "১২৩ মেইন স্ট্রিট",
            "post_office": "SomePostOffice",
            "upazila": "SomeUpazila",
            "district": "SomeDistrict",
            "number": "১২৩৪৫৬৭৮৯০",
            "parent_number": "০৯৮৭৬৫৪৩২১",
            "blood_group": "A+",
            "technology_code": "CS001",
            "semester": "১ম",
            "birth_date": "2000-01-01",
            "ssc_roll": "SSC001",
            "image": None,
            "signature": None,
            "parent_signature": None,
            "policy_agreement": True,
            "is_active": False
        }
    },{
        "model": "auth.user",
        "pk": 14,
        "fields": {
            "username": "john_doe14",
            "password": "pbkdf2_sha256$150000$...$...",
            "email": "john@example.com",
            "is_staff": False,
            "is_superuser": False
        }
    },
    {
        "model": "accounts.studentprofile",
        "pk": 14,
        "fields": {
            "user": 14,
            "shift": "বিকেল",
            "department": "কম্পিউটার বিজ্ঞান",
            "roll": "001",
            "name": "জন ডো",
            "father_name": "রিচার্ড ডো",
            "mother_name": "জেন ডো",
            "address": "১২৩ মেইন স্ট্রিট",
            "post_office": "SomePostOffice",
            "upazila": "SomeUpazila",
            "district": "SomeDistrict",
            "number": "১২৩৪৫৬৭৮৯০",
            "parent_number": "০৯৮৭৬৫৪৩২১",
            "blood_group": "A+",
            "technology_code": "CS001",
            "semester": "১ম",
            "birth_date": "2000-01-01",
            "ssc_roll": "SSC001",
            "image": None,
            "signature": None,
            "parent_signature": None,
            "policy_agreement": True,
            "is_active": False
        }
    },{
        "model": "auth.user",
        "pk": 15,
        "fields": {
            "username": "john_doe15",
            "password": "pbkdf2_sha256$150000$...$...",
            "email": "john@example.com",
            "is_staff": False,
            "is_superuser": False
        }
    },
    {
        "model": "accounts.studentprofile",
        "pk": 15,
        "fields": {
            "user": 15,
            "shift": "বিকেল",
            "department": "কম্পিউটার বিজ্ঞান",
            "roll": "001",
            "name": "জন ডো",
            "father_name": "রিচার্ড ডো",
            "mother_name": "জেন ডো",
            "address": "১২৩ মেইন স্ট্রিট",
            "post_office": "SomePostOffice",
            "upazila": "SomeUpazila",
            "district": "SomeDistrict",
            "number": "১২৩৪৫৬৭৮৯০",
            "parent_number": "০৯৮৭৬৫৪৩২১",
            "blood_group": "A+",
            "technology_code": "CS001",
            "semester": "১ম",
            "birth_date": "2000-01-01",
            "ssc_roll": "SSC001",
            "image": None,
            "signature": None,
            "parent_signature": None,
            "policy_agreement": True,
            "is_active": False
        }
    },{
        "model": "auth.user",
        "pk": 16,
        "fields": {
            "username": "john_doe16",
            "password": "pbkdf2_sha256$150000$...$...",
            "email": "john@example.com",
            "is_staff": False,
            "is_superuser": False
        }
    },
    {
        "model": "accounts.studentprofile",
        "pk": 16,
        "fields": {
            "user": 16,
            "shift": "বিকেল",
            "department": "কম্পিউটার বিজ্ঞান",
            "roll": "001",
            "name": "জন ডো",
            "father_name": "রিচার্ড ডো",
            "mother_name": "জেন ডো",
            "address": "১২৩ মেইন স্ট্রিট",
            "post_office": "SomePostOffice",
            "upazila": "SomeUpazila",
            "district": "SomeDistrict",
            "number": "১২৩৪৫৬৭৮৯০",
            "parent_number": "০৯৮৭৬৫৪৩২১",
            "blood_group": "A+",
            "technology_code": "CS001",
            "semester": "১ম",
            "birth_date": "2000-01-01",
            "ssc_roll": "SSC001",
            "image": None,
            "signature": None,
            "parent_signature": None,
            "policy_agreement": True,
            "is_active": False
        }
    },{
        "model": "auth.user",
        "pk": 17,
        "fields": {
            "username": "john_doe17",
            "password": "pbkdf2_sha256$150000$...$...",
            "email": "john@example.com",
            "is_staff": False,
            "is_superuser": False
        }
    },
    {
        "model": "accounts.studentprofile",
        "pk": 17,
        "fields": {
            "user": 17,
            "shift": "বিকেল",
            "department": "কম্পিউটার বিজ্ঞান",
            "roll": "001",
            "name": "জন ডো",
            "father_name": "রিচার্ড ডো",
            "mother_name": "জেন ডো",
            "address": "১২৩ মেইন স্ট্রিট",
            "post_office": "SomePostOffice",
            "upazila": "SomeUpazila",
            "district": "SomeDistrict",
            "number": "১২৩৪৫৬৭৮৯০",
            "parent_number": "০৯৮৭৬৫৪৩২১",
            "blood_group": "A+",
            "technology_code": "CS001",
            "semester": "১ম",
            "birth_date": "2000-01-01",
            "ssc_roll": "SSC001",
            "image": None,
            "signature": None,
            "parent_signature": None,
            "policy_agreement": True,
            "is_active": False
        }
    },{
        "model": "auth.user",
        "pk": 18,
        "fields": {
            "username": "john_doe18",
            "password": "pbkdf2_sha256$150000$...$...",
            "email": "john@example.com",
            "is_staff": False,
            "is_superuser": False
        }
    },
    {
        "model": "accounts.studentprofile",
        "pk": 18,
        "fields": {
            "user": 18,
            "shift": "বিকেল",
            "department": "কম্পিউটার বিজ্ঞান",
            "roll": "001",
            "name": "জন ডো",
            "father_name": "রিচার্ড ডো",
            "mother_name": "জেন ডো",
            "address": "১২৩ মেইন স্ট্রিট",
            "post_office": "SomePostOffice",
            "upazila": "SomeUpazila",
            "district": "SomeDistrict",
            "number": "১২৩৪৫৬৭৮৯০",
            "parent_number": "০৯৮৭৬৫৪৩২১",
            "blood_group": "A+",
            "technology_code": "CS001",
            "semester": "১ম",
            "birth_date": "2000-01-01",
            "ssc_roll": "SSC001",
            "image": None,
            "signature": None,
            "parent_signature": None,
            "policy_agreement": True,
            "is_active": False
        }
    },{
        "model": "auth.user",
        "pk": 19,
        "fields": {
            "username": "john_doe19",
            "password": "pbkdf2_sha256$150000$...$...",
            "email": "john@example.com",
            "is_staff": False,
            "is_superuser": False
        }
    },
    {
        "model": "accounts.studentprofile",
        "pk": 19,
        "fields": {
            "user": 19,
            "shift": "বিকেল",
            "department": "কম্পিউটার বিজ্ঞান",
            "roll": "001",
            "name": "জন ডো",
            "father_name": "রিচার্ড ডো",
            "mother_name": "জেন ডো",
            "address": "১২৩ মেইন স্ট্রিট",
            "post_office": "SomePostOffice",
            "upazila": "SomeUpazila",
            "district": "SomeDistrict",
            "number": "১২৩৪৫৬৭৮৯০",
            "parent_number": "০৯৮৭৬৫৪৩২১",
            "blood_group": "A+",
            "technology_code": "CS001",
            "semester": "১ম",
            "birth_date": "2000-01-01",
            "ssc_roll": "SSC001",
            "image": None,
            "signature": None,
            "parent_signature": None,
            "policy_agreement": True,
            "is_active": False
        }
    },{
        "model": "auth.user",
        "pk": 20,
        "fields": {
            "username": "john_doe20",
            "password": "pbkdf2_sha256$150000$...$...",
            "email": "john@example.com",
            "is_staff": False,
            "is_superuser": False
        }
    },
    {
        "model": "accounts.studentprofile",
        "pk": 20,
        "fields": {
            "user": 20,
            "shift": "বিকেল",
            "department": "কম্পিউটার বিজ্ঞান",
            "roll": "001",
            "name": "জন ডো",
            "father_name": "রিচার্ড ডো",
            "mother_name": "জেন ডো",
            "address": "১২৩ মেইন স্ট্রিট",
            "post_office": "SomePostOffice",
            "upazila": "SomeUpazila",
            "district": "SomeDistrict",
            "number": "১২৩৪৫৬৭৮৯০",
            "parent_number": "০৯৮৭৬৫৪৩২১",
            "blood_group": "A+",
            "technology_code": "CS001",
            "semester": "১ম",
            "birth_date": "2000-01-01",
            "ssc_roll": "SSC001",
            "image": None,
            "signature": None,
            "parent_signature": None,
            "policy_agreement": True,
            "is_active": False
        }
    },{
        "model": "auth.user",
        "pk": 21,
        "fields": {
            "username": "john_doe21",
            "password": "pbkdf2_sha256$150000$...$...",
            "email": "john@example.com",
            "is_staff": False,
            "is_superuser": False
        }
    },
    {
        "model": "accounts.studentprofile",
        "pk": 21,
        "fields": {
            "user": 21,
            "shift": "বিকেল",
            "department": "কম্পিউটার বিজ্ঞান",
            "roll": "001",
            "name": "জন ডো",
            "father_name": "রিচার্ড ডো",
            "mother_name": "জেন ডো",
            "address": "১২৩ মেইন স্ট্রিট",
            "post_office": "SomePostOffice",
            "upazila": "SomeUpazila",
            "district": "SomeDistrict",
            "number": "১২৩৪৫৬৭৮৯০",
            "parent_number": "০৯৮৭৬৫৪৩২১",
            "blood_group": "A+",
            "technology_code": "CS001",
            "semester": "১ম",
            "birth_date": "2000-01-01",
            "ssc_roll": "SSC001",
            "image": None,
            "signature": None,
            "parent_signature": None,
            "policy_agreement": True,
            "is_active": False
        }
    },{
        "model": "auth.user",
        "pk": 22,
        "fields": {
            "username": "john_doe22",
            "password": "pbkdf2_sha256$150000$...$...",
            "email": "john@example.com",
            "is_staff": False,
            "is_superuser": False
        }
    },
    {
        "model": "accounts.studentprofile",
        "pk": 22,
        "fields": {
            "user": 22,
            "shift": "বিকেল",
            "department": "কম্পিউটার বিজ্ঞান",
            "roll": "001",
            "name": "জন ডো",
            "father_name": "রিচার্ড ডো",
            "mother_name": "জেন ডো",
            "address": "১২৩ মেইন স্ট্রিট",
            "post_office": "SomePostOffice",
            "upazila": "SomeUpazila",
            "district": "SomeDistrict",
            "number": "১২৩৪৫৬৭৮৯০",
            "parent_number": "০৯৮৭৬৫৪৩২১",
            "blood_group": "A+",
            "technology_code": "CS001",
            "semester": "১ম",
            "birth_date": "2000-01-01",
            "ssc_roll": "SSC001",
            "image": None,
            "signature": None,
            "parent_signature": None,
            "policy_agreement": True,
            "is_active": False
        }
    },{
        "model": "auth.user",
        "pk": 23,
        "fields": {
            "username": "john_doe23",
            "password": "pbkdf2_sha256$150000$...$...",
            "email": "john@example.com",
            "is_staff": False,
            "is_superuser": False
        }
    },
    {
        "model": "accounts.studentprofile",
        "pk": 23,
        "fields": {
            "user": 23,
            "shift": "বিকেল",
            "department": "কম্পিউটার বিজ্ঞান",
            "roll": "001",
            "name": "জন ডো",
            "father_name": "রিচার্ড ডো",
            "mother_name": "জেন ডো",
            "address": "১২৩ মেইন স্ট্রিট",
            "post_office": "SomePostOffice",
            "upazila": "SomeUpazila",
            "district": "SomeDistrict",
            "number": "১২৩৪৫৬৭৮৯০",
            "parent_number": "০৯৮৭৬৫৪৩২১",
            "blood_group": "A+",
            "technology_code": "CS001",
            "semester": "১ম",
            "birth_date": "2000-01-01",
            "ssc_roll": "SSC001",
            "image": None,
            "signature": None,
            "parent_signature": None,
            "policy_agreement": True,
            "is_active": False
        }
    },{
        "model": "auth.user",
        "pk": 24,
        "fields": {
            "username": "john_doe24",
            "password": "pbkdf2_sha256$150000$...$...",
            "email": "john@example.com",
            "is_staff": False,
            "is_superuser": False
        }
    },
    {
        "model": "accounts.studentprofile",
        "pk": 24,
        "fields": {
            "user": 24,
            "shift": "বিকেল",
            "department": "কম্পিউটার বিজ্ঞান",
            "roll": "001",
            "name": "জন ডো",
            "father_name": "রিচার্ড ডো",
            "mother_name": "জেন ডো",
            "address": "১২৩ মেইন স্ট্রিট",
            "post_office": "SomePostOffice",
            "upazila": "SomeUpazila",
            "district": "SomeDistrict",
            "number": "১২৩৪৫৬৭৮৯০",
            "parent_number": "০৯৮৭৬৫৪৩২১",
            "blood_group": "A+",
            "technology_code": "CS001",
            "semester": "১ম",
            "birth_date": "2000-01-01",
            "ssc_roll": "SSC001",
            "image": None,
            "signature": None,
            "parent_signature": None,
            "policy_agreement": True,
            "is_active": False
        }
    },{
        "model": "auth.user",
        "pk": 25,
        "fields": {
            "username": "john_doe25",
            "password": "pbkdf2_sha256$150000$...$...",
            "email": "john@example.com",
            "is_staff": False,
            "is_superuser": False
        }
    },
    {
        "model": "accounts.studentprofile",
        "pk": 25,
        "fields": {
            "user": 25,
            "shift": "বিকেল",
            "department": "কম্পিউটার বিজ্ঞান",
            "roll": "001",
            "name": "জন ডো",
            "father_name": "রিচার্ড ডো",
            "mother_name": "জেন ডো",
            "address": "১২৩ মেইন স্ট্রিট",
            "post_office": "SomePostOffice",
            "upazila": "SomeUpazila",
            "district": "SomeDistrict",
            "number": "১২৩৪৫৬৭৮৯০",
            "parent_number": "০৯৮৭৬৫৪৩২১",
            "blood_group": "A+",
            "technology_code": "CS001",
            "semester": "১ম",
            "birth_date": "2000-01-01",
            "ssc_roll": "SSC001",
            "image": None,
            "signature": None,
            "parent_signature": None,
            "policy_agreement": True,
            "is_active": False
        }
    },{
        "model": "auth.user",
        "pk": 26,
        "fields": {
            "username": "john_doe26",
            "password": "pbkdf2_sha256$150000$...$...",
            "email": "john@example.com",
            "is_staff": False,
            "is_superuser": False
        }
    },
    {
        "model": "accounts.studentprofile",
        "pk": 26,
        "fields": {
            "user": 26,
            "shift": "বিকেল",
            "department": "কম্পিউটার বিজ্ঞান",
            "roll": "001",
            "name": "জন ডো",
            "father_name": "রিচার্ড ডো",
            "mother_name": "জেন ডো",
            "address": "১২৩ মেইন স্ট্রিট",
            "post_office": "SomePostOffice",
            "upazila": "SomeUpazila",
            "district": "SomeDistrict",
            "number": "১২৩৪৫৬৭৮৯০",
            "parent_number": "০৯৮৭৬৫৪৩২১",
            "blood_group": "A+",
            "technology_code": "CS001",
            "semester": "১ম",
            "birth_date": "2000-01-01",
            "ssc_roll": "SSC001",
            "image": None,
            "signature": None,
            "parent_signature": None,
            "policy_agreement": True,
            "is_active": False
        }
    },{
        "model": "auth.user",
        "pk": 27,
        "fields": {
            "username": "john_doe27",
            "password": "pbkdf2_sha256$150000$...$...",
            "email": "john@example.com",
            "is_staff": False,
            "is_superuser": False
        }
    },
    {
        "model": "accounts.studentprofile",
        "pk": 27,
        "fields": {
            "user": 27,
            "shift": "বিকেল",
            "department": "কম্পিউটার বিজ্ঞান",
            "roll": "001",
            "name": "জন ডো",
            "father_name": "রিচার্ড ডো",
            "mother_name": "জেন ডো",
            "address": "১২৩ মেইন স্ট্রিট",
            "post_office": "SomePostOffice",
            "upazila": "SomeUpazila",
            "district": "SomeDistrict",
            "number": "১২৩৪৫৬৭৮৯০",
            "parent_number": "০৯৮৭৬৫৪৩২১",
            "blood_group": "A+",
            "technology_code": "CS001",
            "semester": "১ম",
            "birth_date": "2000-01-01",
            "ssc_roll": "SSC001",
            "image": None,
            "signature": None,
            "parent_signature": None,
            "policy_agreement": True,
            "is_active": False
        }
    },{
        "model": "auth.user",
        "pk": 28,
        "fields": {
            "username": "john_doe28",
            "password": "pbkdf2_sha256$150000$...$...",
            "email": "john@example.com",
            "is_staff": False,
            "is_superuser": False
        }
    },
    {
        "model": "accounts.studentprofile",
        "pk": 28,
        "fields": {
            "user": 28,
            "shift": "বিকেল",
            "department": "কম্পিউটার বিজ্ঞান",
            "roll": "001",
            "name": "জন ডো",
            "father_name": "রিচার্ড ডো",
            "mother_name": "জেন ডো",
            "address": "১২৩ মেইন স্ট্রিট",
            "post_office": "SomePostOffice",
            "upazila": "SomeUpazila",
            "district": "SomeDistrict",
            "number": "১২৩৪৫৬৭৮৯০",
            "parent_number": "০৯৮৭৬৫৪৩২১",
            "blood_group": "A+",
            "technology_code": "CS001",
            "semester": "১ম",
            "birth_date": "2000-01-01",
            "ssc_roll": "SSC001",
            "image": None,
            "signature": None,
            "parent_signature": None,
            "policy_agreement": True,
            "is_active": False
        }
    },{
        "model": "auth.user",
        "pk": 29,
        "fields": {
            "username": "john_doe29",
            "password": "pbkdf2_sha256$150000$...$...",
            "email": "john@example.com",
            "is_staff": False,
            "is_superuser": False
        }
    },
    {
        "model": "accounts.studentprofile",
        "pk": 29,
        "fields": {
            "user": 29,
            "shift": "বিকেল",
            "department": "কম্পিউটার বিজ্ঞান",
            "roll": "001",
            "name": "জন ডো",
            "father_name": "রিচার্ড ডো",
            "mother_name": "জেন ডো",
            "address": "১২৩ মেইন স্ট্রিট",
            "post_office": "SomePostOffice",
            "upazila": "SomeUpazila",
            "district": "SomeDistrict",
            "number": "১২৩৪৫৬৭৮৯০",
            "parent_number": "০৯৮৭৬৫৪৩২১",
            "blood_group": "A+",
            "technology_code": "CS001",
            "semester": "১ম",
            "birth_date": "2000-01-01",
            "ssc_roll": "SSC001",
            "image": None,
            "signature": None,
            "parent_signature": None,
            "policy_agreement": True,
            "is_active": False
        }
    },{
        "model": "auth.user",
        "pk": 30,
        "fields": {
            "username": "john_doe30",
            "password": "pbkdf2_sha256$150000$...$...",
            "email": "john@example.com",
            "is_staff": False,
            "is_superuser": False
        }
    },
    {
        "model": "accounts.studentprofile",
        "pk": 30,
        "fields": {
            "user": 30,
            "shift": "বিকেল",
            "department": "কম্পিউটার বিজ্ঞান",
            "roll": "001",
            "name": "জন ডো",
            "father_name": "রিচার্ড ডো",
            "mother_name": "জেন ডো",
            "address": "১২৩ মেইন স্ট্রিট",
            "post_office": "SomePostOffice",
            "upazila": "SomeUpazila",
            "district": "SomeDistrict",
            "number": "১২৩৪৫৬৭৮৯০",
            "parent_number": "০৯৮৭৬৫৪৩২১",
            "blood_group": "A+",
            "technology_code": "CS001",
            "semester": "১ম",
            "birth_date": "2000-01-01",
            "ssc_roll": "SSC001",
            "image": None,
            "signature": None,
            "parent_signature": None,
            "policy_agreement": True,
            "is_active": False
        }
    },{
        "model": "auth.user",
        "pk": 31,
        "fields": {
            "username": "john_doe31",
            "password": "pbkdf2_sha256$150000$...$...",
            "email": "john@example.com",
            "is_staff": False,
            "is_superuser": False
        }
    },
    {
        "model": "accounts.studentprofile",
        "pk": 31,
        "fields": {
            "user": 31,
            "shift": "বিকেল",
            "department": "কম্পিউটার বিজ্ঞান",
            "roll": "001",
            "name": "জন ডো",
            "father_name": "রিচার্ড ডো",
            "mother_name": "জেন ডো",
            "address": "১২৩ মেইন স্ট্রিট",
            "post_office": "SomePostOffice",
            "upazila": "SomeUpazila",
            "district": "SomeDistrict",
            "number": "১২৩৪৫৬৭৮৯০",
            "parent_number": "০৯৮৭৬৫৪৩২১",
            "blood_group": "A+",
            "technology_code": "CS001",
            "semester": "১ম",
            "birth_date": "2000-01-01",
            "ssc_roll": "SSC001",
            "image": None,
            "signature": None,
            "parent_signature": None,
            "policy_agreement": True,
            "is_active": False
        }
    }
]

with open('students_fixture.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
