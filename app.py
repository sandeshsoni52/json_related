from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Load the JSON data once when the app starts
data = {
    "Programs": {
        "Under Graduate Programs": {
            "Engineering & Technology": {
                "Jawaharlal Nehru Engineering College": {
                    "B Tech": [
                        "Chemical Engineering",
                        "Civil Engineering",
                        "Computer Science and Engineering",
                        "Electrical and Computer Engineering",
                        "Mechanical Engineering",
                        "Robotics and Artificial Intelligence",
                        "Mechanical and Mechatronics Engineering (Additive Manufacturing)",
                        "Electronics and Computer Engineering",
                        "Artificial Intelligence & Data Science"
                    ],
                    "Bachelor": [
                        "Architecture"
                    ]
                },
                "Institute of Fire Service Engineering": {
                    "B Sc": [
                        "Fire and Safety"
                    ]
                },
                "University Department of Information and Communication Technology (UDICT)": {
                    "B Tech": [
                        "Information Technology",
                        "AI & ML",
                        "Data Science"
                    ]
                },
                "School of Engineering & Technology": {
                    "B Tech": [
                        "Agriculture Engineering",
                        "Computer Science & Engineering (IoT, Cyber Security)",
                        "Electrical and Instrumentation Engineering",
                        "(Integrated) Civil Engineering with Computer Application",
                        "(Integrated) Computer Science and Engineering (Data Science)",
                        "(Integrated) Computer Science and Engineering (IoT)",
                        "(Integrated) Advanced Mechatronics and Industrial Automation",
                        "(Integrated) Robotics and AI",
                        "Electronic Engineering (VLSI Design and Technology)",
                        "(Integrated) Information Technology",
                        "(Integrated) Electrical and Computer Engineering",
                        "Computer Science and Design",
                        "Robotics and Automation"
                    ]
                },
                "University Department of Pharmaceutical Sciences": {
                    "Bachelor": [
                        "Pharmacy"
                    ]
                }
            },
            "Management & Commerce": {
                "Institute of Management & Research": {
                    "BBA": [
                        "Hons./ Hons. with Research",
                        "Hons./ Hons. with Research in FinTech",
                        "Hons./ Hons. with Research in Business Analytics"
                    ],
                    "B Com": [
                        "Hons./ Hons. with Research"
                    ]
                },
                "Institute of Hotel Management": {
                    "B Sc": [
                        "Hons. Hotel Operations Catering Services"
                    ],
                    "BBA": [
                        "Hons. in Aviation, Hospitality and Travel & Tourism"
                    ],
                    "B Sc": [
                        "Hons. Culinary Arts"
                    ]
                },
                "Nath School of Business & Technology": {
                    "Bachelor": [
                        "Management Studies (BMS)"
                    ],
                    "BCA": [
                        "Cloud Technology & Information Security"
                    ],
                    "MCA": [
                        "Digital Product Technology",
                        "Artificial Intelligence - Data Science"
                    ],
                    "BMS": [
                        "Entrepreneurship, Family Business and Innovation"
                    ]
                }
            },
            "Basic & Applied Science": {
                "Dr. G.Y. Pathrikar College of Computer Science & Information Technology": {
                    "B Sc": [
                        "Hons. Computer Science",
                        "Hons. Information Technology",
                        "Hons. Science",
                        "Hons. Animation",
                        "Hons. Robotics",
                        "Hons. Digital Marketing",
                        "M Sc. Data Science (Integrated)"
                    ]
                },
                "Institute of Bioscience and Technology": {
                    "B Sc": [
                        "Hons. Biotechnology",
                        "Hons. Bioinformatics",
                        "Hons. Microbiology",
                        "Hons. Food Technology & Processing",
                        "Hons. Food Nutrition & Dietetics"
                    ],
                    "B Tech": [
                        "Biotechnology",
                        "Food Processing Technology",
                        "Biomedical Engineering"
                    ]
                },
                "School of Basic & Applied Science": {
                    "B Sc": [
                        "Hons. Physics",
                        "Hons. Chemistry",
                        "Hons. Mathematics",
                        "Hons. Statistics",
                        "Hons. Geology",
                        "Hons. Home Science",
                        "Hons. Environmental Science",
                        "Hons. Zoology",
                        "Hons. Forensic Science"
                    ],
                    "B Tech": [
                        "Cosmetic Technology"
                    ]
                }
            },
            "Social Science & Humanities": {
                "College of Journalism & Mass Communication": {
                    "B A": [
                        "International Journalism & Electronic Media",
                        "Hons./Reg. with Research in Mass Communication and Media"
                    ]
                },
                "Institute of Social Sciences": {
                    "Bachelor": [
                        "Social Work (BSW)"
                    ],
                    "B A": [
                        "Hons. Psychology",
                        "Hons. Economics"
                    ]
                },
                "School of Film Arts": {
                    "B A": [
                        "Hons. Cinematography",
                        "Hons. Film Direction",
                        "Hons. Film Editing",
                        "Hons. Sound Designing & Music Production",
                        "Hons. VFX and Animation",
                        "Hons. Film Acting",
                        "Hons. Production Design & Art Direction"
                    ]
                },
                "Department of Photography": {
                    "B A": [
                        "Hons. Photography"
                    ]
                },
                "Institute of Indian & Foreign Languages": {
                    "B A": [
                        "Hons. English"
                    ]
                },
                "School of Legal Studies & Research": {
                    "Bachelor": [
                        "Law (LL.B.)"
                    ],
                    "BBA": [
                        "Bachelor of Business Administration and Bachelor of Law"
                    ]
                }
            },
            "Interdisciplinary Studies": {
                "Department of Sports, Physical Education & Yog Science": {
                    "B P E S": [
                        "Bachelor of Physical Education & Sports"
                    ]
                },
                "Department of Education": {
                    "B A": [
                        "Hons. Education"
                    ]
                },
                "University Department of Music & Theatre": {
                    "BPA": [
                        "Music",
                        "Theatre"
                    ]
                }
            },
            "Design": {
                "Leonardo Da Vinci School of Design": {
                    "BFA": [
                        "Applied Art",
                        "Contemporary Art",
                        "Traditional Art and Craft"
                    ],
                    "B Des": [
                        "Interior Design",
                        "Fashion Design",
                        "Textile Design",
                        "Industrial Design",
                        "Visual Communication"
                    ]
                }
            },
            "Performing Arts": {
                "MAHAGAMI GURUKUL Center for Performing Arts": {
                    "BPA": [
                        "Kathak (Lab and Kathak)",
                        "Odissi (Lab and Gurukul)"
                    ]
                }
            }
        },
        "Post Graduate Programs": {
            "Engineering & Technology": {
                "Jawaharlal Nehru Engineering College": {
                    "B Tech": [
                        "Chemical Engineering",
                        "Civil Engineering",
                        "Computer Science and Engineering",
                        "Electrical and Computer Engineering",
                        "Mechanical Engineering",
                        "Robotics and Artificial Intelligence",
                        "Mechanical and Mechatronics Engineering (Additive Manufacturing)",
                        "Electronics and Computer Engineering",
                        "Artificial Intelligence & Data Science"
                    ],
                    "Bachelor": [
                        "Architecture"
                    ]
                },
                "Institute of Fire Service Engineering": {
                    "B Sc": [
                        "Fire and Safety"
                    ]
                },
                "University Department of Information and Communication Technology (UDICT)": {
                    "B Tech": [
                        "Information Technology",
                        "AI & ML",
                        "Data Science"
                    ]
                },
                "School of Engineering & Technology": {
                    "B Tech": [
                        "Agriculture Engineering",
                        "Computer Science & Engineering (IoT, Cyber Security)",
                        "Electrical and Instrumentation Engineering",
                        "(Integrated) Civil Engineering with Computer Application",
                        "(Integrated) Computer Science and Engineering (Data Science)",
                        "(Integrated) Computer Science and Engineering (IoT)",
                        "(Integrated) Advanced Mechatronics and Industrial Automation",
                        "(Integrated) Robotics and AI",
                        "Electronic Engineering (VLSI Design and Technology)",
                        "(Integrated) Information Technology",
                        "(Integrated) Electrical and Computer Engineering",
                        "Computer Science and Design",
                        "Robotics and Automation"
                    ]
                },
                "University Department of Pharmaceutical Sciences": {
                    "Bachelor": [
                        "Pharmacy"
                    ]
                }
            },
            "Management & Commerce": {
                "Institute of Management & Research": {
                    "BBA": [
                        "Hons./ Hons. with Research",
                        "Hons./ Hons. with Research in FinTech",
                        "Hons./ Hons. with Research in Business Analytics"
                    ],
                    "B Com": [
                        "Hons./ Hons. with Research"
                    ]
                },
                "Institute of Hotel Management": {
                    "B Sc": [
                        "Hons. Hotel Operations Catering Services"
                    ],
                    "BBA": [
                        "Hons. in Aviation, Hospitality and Travel & Tourism"
                    ],
                    "B Sc": [
                        "Hons. Culinary Arts"
                    ]
                },
                "Nath School of Business & Technology": {
                    "Bachelor": [
                        "Management Studies (BMS)"
                    ],
                    "BCA": [
                        "Cloud Technology & Information Security"
                    ],
                    "MCA": [
                        "Digital Product Technology",
                        "Artificial Intelligence - Data Science"
                    ],
                    "BMS": [
                        "Entrepreneurship, Family Business and Innovation"
                    ]
                }
            },
            "Basic & Applied Science": {
                "Dr. G.Y. Pathrikar College of Computer Science & Information Technology": {
                    "B Sc": [
                        "Hons. Computer Science",
                        "Hons. Information Technology",
                        "Hons. Science",
                        "Hons. Animation",
                        "Hons. Robotics",
                        "Hons. Digital Marketing",
                        "M Sc. Data Science (Integrated)"
                    ]
                },
                "Institute of Bioscience and Technology": {
                    "B Sc": [
                        "Hons. Biotechnology",
                        "Hons. Bioinformatics",
                        "Hons. Microbiology",
                        "Hons. Food Technology & Processing",
                        "Hons. Food Nutrition & Dietetics"
                    ],
                    "B Tech": [
                        "Biotechnology",
                        "Food Processing Technology",
                        "Biomedical Engineering"
                    ]
                },
                "School of Basic & Applied Science": {
                    "B Sc": [
                        "Hons. Physics",
                        "Hons. Chemistry",
                        "Hons. Mathematics",
                        "Hons. Statistics",
                        "Hons. Geology",
                        "Hons. Home Science",
                        "Hons. Environmental Science",
                        "Hons. Zoology",
                        "Hons. Forensic Science"
                    ],
                    "B Tech": [
                        "Cosmetic Technology"
                    ]
                }
            },
            "Social Science & Humanities": {
                "College of Journalism & Mass Communication": {
                    "B A": [
                        "International Journalism & Electronic Media",
                        "Hons./Reg. with Research in Mass Communication and Media"
                    ]
                },
                "Institute of Social Sciences": {
                    "Bachelor": [
                        "Social Work (BSW)"
                    ],
                    "B A": [
                        "Hons. Psychology",
                        "Hons. Economics"
                    ]
                },
                "School of Film Arts": {
                    "B A": [
                        "Hons. Cinematography",
                        "Hons. Film Direction",
                        "Hons. Film Editing",
                        "Hons. Sound Designing & Music Production",
                        "Hons. VFX and Animation",
                        "Hons. Film Acting",
                        "Hons. Production Design & Art Direction"
                    ]
                },
                "Department of Photography": {
                    "B A": [
                        "Hons. Photography"
                    ]
                },
                "Institute of Indian & Foreign Languages": {
                    "B A": [
                        "Hons. English"
                    ]
                },
                "School of Legal Studies & Research": {
                    "Bachelor": [
                        "Law (LL.B.)"
                    ],
                    "BBA": [
                        "Bachelor of Business Administration and Bachelor of Law"
                    ]
                }
            },
            "Interdisciplinary Studies": {
                "Department of Sports, Physical Education & Yog Science": {
                    "B P E S": [
                        "Bachelor of Physical Education & Sports"
                    ]
                },
                "Department of Education": {
                    "B A": [
                        "Hons. Education"
                    ]
                },
                "University Department of Music & Theatre": {
                    "BPA": [
                        "Music",
                        "Theatre"
                    ]
                }
            },
            "Design": {
                "Leonardo Da Vinci School of Design": {
                    "BFA": [
                        "Applied Art",
                        "Contemporary Art",
                        "Traditional Art and Craft"
                    ],
                    "B Des": [
                        "Interior Design",
                        "Fashion Design",
                        "Textile Design",
                        "Industrial Design",
                        "Visual Communication"
                    ]
                }
            },
            "Performing Arts": {
                "MAHAGAMI GURUKUL Center for Performing Arts": {
                    "BPA": [
                        "Kathak (Lab and Kathak)",
                        "Odissi (Lab and Gurukul)"
                    ]
                }
            }
        }

    
    }


}
@app.route('/data', methods=['GET'])
def get_all_data():
    return jsonify(data)

@app.route('/data/<program_type>', methods=['GET'])
def get_program_type(program_type):
    program_type = program_type.replace("-", " ")  # Handle spaces in URLs
    filtered_data = data["Programs"].get(program_type.title())
    if filtered_data:
        return jsonify({program_type: filtered_data})
    else:
        return jsonify({"error": "Program type not found"}), 404

@app.route('/data/<program_type>/<category>', methods=['GET'])
def get_category(program_type, category):
    program_type = program_type.replace("-", " ")  # Handle spaces in URLs
    category = category.replace("-", " ")  # Handle spaces in URLs
    program_data = data["Programs"].get(program_type.title())
    if program_data and category in program_data:
        return jsonify({category: program_data[category]})
    else:
        return jsonify({"error": "Sub-program not found"}), 404

@app.route('/data/<program_type>/<category>/<institute>', methods=['GET'])
def get_institute(program_type, category, institute):
    program_type = program_type.replace("-", " ")  # Handle spaces in URLs
    category = category.replace("-", " ")  # Handle spaces in URLs
    institute = institute.replace("-", " ")  # Handle spaces in URLs

    program_data = data["Programs"].get(program_type.title())
    if program_data:
        category_data = program_data.get(category)
        if category_data:
            institute_data = category_data.get(institute)
            if institute_data:
                return jsonify({institute: institute_data})
            else:
                return jsonify({"error": f"Institute '{institute}' not found in category '{category}'"}), 404
        else:
            return jsonify({"error": f"Category '{category}' not found in program type '{program_type}'"}), 404
    else:
        return jsonify({"error": f"Program type '{program_type}' not found"}), 404

@app.route('/data/<program_type>/<category>/<institute>/<degree>', methods=['GET'])
def get_degree_programs(program_type, category, institute, degree):
    program_type = program_type.replace("-", " ")  # Handle spaces in URLs
    category = category.replace("-", " ")  # Handle spaces in URLs
    institute = institute.replace("-", " ")  # Handle spaces in URLs
    degree = degree.replace("-", " ")  # Handle spaces in URLs

    program_data = data["Programs"].get(program_type.title())
    if program_data:
        category_data = program_data.get(category)
        if category_data:
            institute_data = category_data.get(institute)
            if institute_data:
                degree_data = institute_data.get(degree)
                if degree_data:
                    return jsonify({degree: degree_data})
                else:
                    return jsonify({"error": f"Degree '{degree}' not found in institute '{institute}'"}), 404
            else:
                return jsonify({"error": f"Institute '{institute}' not found in category '{category}'"}), 404
        else:
            return jsonify({"error": f"Category '{category}' not found in program type '{program_type}'"}), 404
    else:
        return jsonify({"error": f"Program type '{program_type}' not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=8000)
